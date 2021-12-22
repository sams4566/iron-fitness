from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import OrderForm
from django.conf import settings
from basket.contexts import basket_contents
from items.models import Item
from .models import OrderItem, Order

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method != 'POST':
        stripe.api_key = stripe_secret_key
        currency = settings.STRIPE_CURRENCY
        present_basket = basket_contents(request)
        total_cost = present_basket['total']
        stripe_total = round(total_cost * 100)
        intent = stripe.PaymentIntent.create(
            currency=currency,
            amount=stripe_total, 
        )
        basket = request.session.get('basket', {})
        order_form = OrderForm()
        print(intent)

    else:
        basket = request.session.get('basket', {})

        form_info = {
            'customer_name': request.POST['customer_name'],
            'telephone': request.POST['telephone'],
            'email': request.POST['email'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }
        order_form = OrderForm(form_info)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order_form.order_number = order.add_order_number()
            order_cost = 0
            for item_id, item_info in basket.items():
                item = get_object_or_404(Item, pk=item_id)
                for size, quantity in item_info['chosen_sizes'].items():
                    item_cost = item.cost
                    order_cost += item_cost
                    order_item = OrderItem(
                        item=item,
                        item_size=size,
                        quantity=quantity,
                        order=order,
                        item_cost=item_cost,
                    )
                    order_item.save()
            order.order_cost = order_cost
            order = order_form.save()
            order_number = order.order_number
        return redirect('checkout_confirmation', order_number=order_number)

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_confirmation(request, order_number):
    del request.session['basket']
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_confirmation.html'
    context = {
        'order': order,
    }
    return render(request, template, context)