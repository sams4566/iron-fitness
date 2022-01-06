from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Item, Category, Review, Rating
from .forms import ItemForm, ReviewForm 


def all_items(request):
    items = Item.objects.all()
    if 'category' in request.GET: 
            category = request.GET['category'].split(',')
            items = items.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)[0]
            template = 'items/all_items.html'
            context = {
                'items': items,
                'category': category,
            }
            return render(request, template, context)
    else:
        items = list(Item.objects.all())
        def sort_item(item):
            return item.name
        items.sort(key=sort_item)
        all_products_category = 'All Products'
    template = 'items/all_items.html'
    context = {
        'items': items,
        'all_products_category': all_products_category,
    }
    return render(request, template, context)


def item_info(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    category = item.category
    user_id = request.user
    similar_items = Item.objects.all().filter(category=category).exclude(id=item_id)
    reviews = item.item_review.order_by('review_date')
    form = ReviewForm()
    template = 'items/item_info.html'
    if request.method == "POST": 
        form = ReviewForm(request.POST, instance=item)
        if form.is_valid():
            review = Review()
            review.item = item
            review.user = request.user
            review.body = form.cleaned_data["body"]
            review.save()
            return redirect('item_info', item_id=item_id)
    if not Rating.objects.filter(user=user_id, item=item).exists():
        rating = Rating()
        rating.item = item
        rating.user = request.user
        rating.save()
    rating_id = Rating.objects.filter(user=user_id, item=item)[0].id
    rating = get_object_or_404(Rating, pk=rating_id)
    one_star = False
    two_stars = False
    if rating.one_star == 1:
        one_star = True
    if rating.two_stars == 2:
        two_stars = True
    context = {
        'item': item,
        'similar_items': similar_items,
        'reviews': reviews,
        'form': form,
        'one_star': one_star,
        'two_stars': two_stars,
    }
    return render(request, template, context)


def one_star(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    user_id = request.user
    rating_id = Rating.objects.filter(user=user_id, item=item)[0].id
    rating = get_object_or_404(Rating, pk=rating_id)
    if rating.one_star == None:
        rating.one_star = 1
        rating.two_stars = 0
        rating.save()
    else:
        rating.one_star = None
        rating.two_stars = None
        rating.save()
    return redirect('item_info', item_id=item_id)


def two_stars(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    user_id = request.user
    rating_id = Rating.objects.filter(user=user_id, item=item)[0].id
    rating = get_object_or_404(Rating, pk=rating_id)
    if rating.two_stars == None:
        rating.two_stars = 2
        rating.one_star = 0
        rating.save()
    else:
        rating.two_stars = None
        rating.one_star = None
        rating.save()
    return redirect('item_info', item_id=item_id)


























def add_item(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            return redirect('item_info', item_id=item.id)
    template = 'items/add_item.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    form = ItemForm(instance=item)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        # print('form is valid', form.is_valid())
        # print(request.POST)
        # print(form)
        # print(dir(form))
        # print(form.data)
        if form.is_valid():
            item = form.save()
            return redirect('item_info', item_id=item.id)
    template = 'items/edit_item.html'
    context = {
        'form': form,
        'item': item,
    }
    return render(request, template, context)


def delete_item(request, item_id):
    product = get_object_or_404(Item, pk=item_id)
    product.delete()
    return redirect(reverse('all_items'))


def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    item_id = review.item_id
    review.delete()
    return redirect('item_info', item_id=item_id)