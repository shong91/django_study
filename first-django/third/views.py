from django.shortcuts import render, get_object_or_404
from third.models import Restaurant
from django.core.paginator import Paginator
from third.forms import RestaurantForm
from django.http import HttpResponseRedirect

# Create your views here.
def list(request):
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants, 5)
    page = request.GET.get('page') # /third/list/?page=1
    items = paginator.get_page(page)

    # Reference: Django official Document (https://docs.djangoproject.com/en/3.1/topics/pagination/)
    print('count', paginator.count)
    print('num_pages', paginator.num_pages)
    page1 = paginator.page(1)
    print('has_next()', page1.has_next())
    print('has_previous()', page1.has_previous())
    print('has_other_pages()', page1.has_other_pages())
    print('next_page_number()', page1.next_page_number())


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
        form = RestaurantForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
    elif request.method == 'GET': # 수정 form
        # item = Restaurant.objects.get(pk=request.GET.get('id')) # /third/update/?id=$$$
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form': form})
    return HttpResponseRedirect('/third/list/')


def detail(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        return render(request, 'third/detail.html', {'item': item})
    return HttpResponseRedirect('/third/list/')


def delete(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item.delete()
    return HttpResponseRedirect('/third/list/')