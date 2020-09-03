from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime


# Create your views here.
def index(request):
    # django.shortcuts 을 이용하면 좀 더 간단하다. (template 가져오기, HttpResponse return 을 간략히 할 수 있음)
    # template = loader.get_template("index.html")

    now = datetime.now()
    # 동적으로 view 메서드에서 정리한 변수를 삽입
    context = {
                'current_date': now,
    }

    return render(request, 'first/index.html', context)
    # return HttpResponse(template.render(context, request))


def select(request): # , year
    context = {'number': 5}
    return render(request, 'first/select.html', context)


def result(request):
    context = {'numbers': [1,2,3,4,5,6]}
    return render(request, 'first/result.html', context)