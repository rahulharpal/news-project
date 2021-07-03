from django.urls import path
from newsapp import views

urlpatterns = [
    path('', views.index),
    path('sportsinfo/', views.sportsinfo),
    path('moviesinfo/', views.moviesinfo),
    path('politicsinfo/', views.politicsinfo),
]
