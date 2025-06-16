from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('property/<str:property_id>/', views.property_detail, name='property_detail'),
]