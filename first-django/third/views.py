from django.shortcuts import render, get_object_or_404, redirect
from third.models import Restaurant, Review
from django.core.paginator import Paginator
from third.forms import RestaurantForm, ReviewForm, UpdateRestaurantForm
from django.http import HttpResponseRedirect
from django.db.models import Count, Avg

# Create your views here.
def list(request):
    restaurants = Restaurant.objects.all().annotate(reviews_count=Count('review'))\
        .annotate(average_point=Avg('review__point')) # Aggregation(Count, Avg, Max): 리뷰 수, 평점 함께 가져오기
    paginator = Paginator(restaurants, 5)
    page = request.GET.get('page') # /third/list/?page=1
    items = paginator.get_page(page)

    # Reference: Django official Document (https://docs.djangoproject.com/en/3.1/topics/pagination/)
    # print('count', paginator.count)
    # print('num_pages', paginator.num_pages)
    # page1 = paginator.page(1)
    # print('has_next()', page1.has_next())
    # print('has_previous()', page1.has_previous())
    # print('has_other_pages()', page1.has_other_pages())
    # print('next_page_number()', page1.next_page_number())

    context = {
        'restaurants': items,
        'paginator': paginator
    }
    return render(request, 'third/list.html', context)


def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/third/list/')

    form = RestaurantForm()
    return render(request, 'third/create.html', {'form': form})


def update(request):
    if request.method == 'POST' and 'id' in request.POST: # 수정 로직
        # item = Restaurant.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        password = request.POST.get('password', '')
        form = UpdateRestaurantForm(request.POST, instance=item)
        if form.is_valid() and password == item.password:
            item = form.save()
    elif request.method == 'GET': # 수정 form
        # item = Restaurant.objects.get(pk=request.GET.get('id')) # /third/update/?id=$$$
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))

        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form': form})
    return HttpResponseRedirect('/third/list/')


def detail(request, id):
    if id is not None:
        item = get_object_or_404(Restaurant, pk=id)
        reviews = Review.objects.filter(restaurant=item).all()
        return render(request, 'third/detail.html', {'item': item, 'reviews': reviews})
    return HttpResponseRedirect('/third/list/')


def delete(request, id):
    item = get_object_or_404(Restaurant, pk=id)
    if request.method == 'POST' and 'password' in request.POST:
        if item.password == request.POST.get('password') or item.password is None:
            item.delete()
            return redirect('list')
        return redirect('restaurant-detail', id=id)
    return render(request, 'third/delete.html', {'item': item})


# 리뷰 ==================================================================================================================
def review_create(request, restaurant_id):
    # 리뷰 저장
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('restaurant-detail', id=restaurant_id)

    # 리뷰 폼 - restaurant id 는 폼 초기에 설정되기를 원해
    item = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(initial={'restaurant': item})
    return render(request, 'third/review_create.html', {'form': form, 'item': item})


def review_delete(request, restaurant_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()
    return redirect('restaurant-detail', id=restaurant_id)


def review_list(request):
    reviews = Review.objects.all().select_related().order_by('-created_at') # Query hits : only 1 (join)
    # reviews = Review.objects.all().order_by('-created_at') : Query hits: every calls
    paginator = Paginator(reviews, 10)
    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'reviews': items
    }

    return render(request, 'third/review_list.html', context)
