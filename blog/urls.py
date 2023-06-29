from django.urls import path 
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView, name='home'),
    path('post/<int:pk>/', BlogDetailView, name='post_detail')
]
