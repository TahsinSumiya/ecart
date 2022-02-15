from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="shophome"),
    path('about/', views.about,name="about"),
     path('contact/', views.contact,name="contact"),
      path('tracker/', views.tracker,name="tracker"),
      path('checkout/', views.checkout,name="tracker"),
      
       path("products/<int:myid>", views.productview, name="ProductView"),
]