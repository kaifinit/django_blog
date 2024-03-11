
from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('post/<slug>', views.post, name="post"),
    path('category', views.category, name="category"),
    path('search', views.search, name="search"),
]
