from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post_detail.html', {'post': post})