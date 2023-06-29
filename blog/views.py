from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.http import HttpResponse
# Create your views here.

def BlogListView(request):
    post = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'post': post})

# def BlogDetailView(request):
#     post = Post
#     return render(request, 'post_detail.html', {'post': post})

def BlogDetailView(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post_detail.html', {'post': post})