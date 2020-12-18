from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"), # routes to /blog
    path('about/', views.about, name="blog-about"), # routes to /blog/about
]
