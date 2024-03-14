
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('pages', views.pages, name="pages"),
    path('post/<slug>', views.post, name="post"),
    path('pages/single', views.single, name="single"),
    path('pages/category', views.category, name="category"),
    path('pages/search', views.search, name="search"),
    path('add_posts', views.add_posts, name="add_posts"),
]
