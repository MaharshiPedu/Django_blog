from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),  # blog-home is the name of the path
    path('about/', views.about, name='blog-about')
]