from django.shortcuts import render
from third.models import Restaurant
from django.core.paginator import Paginator


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

