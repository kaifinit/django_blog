
from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('posts/pages/about', views.about, name="about"),
    path('posts/pages/contact', views.contact, name="contact"),
]
