
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('pages', views.pages, name="pages"),
    path('post/<id>', views.post, name="post"),
    path('post/<id>/like', views.like, name="like"),
    path('post/<id>/save', views.save, name="save"),
    path('pages/category', views.category, name="category"),
    path('search', views.search, name="search"),
    path('comment', views.comment, name="comment"),
    path('add_posts', views.add_posts, name="add_posts"),
]
