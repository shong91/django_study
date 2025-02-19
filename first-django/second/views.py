from django.shortcuts import render
from second.models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect


# Create your views here.
def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save() # 레코드 생성
        return HttpResponseRedirect('/second/list/')

    form = PostForm()
    return render(request, 'second/create.html', {'form': form})


def confirm(request):
    form = PostForm(request.POST)
    if form.is_valid():
        return render(request, 'second/confirm.html', {'form': form})
    return HttpResponseRedirect('/second/create/')
