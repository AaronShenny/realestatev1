from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('property/view/<str:property_id>/', views.property_detail, name='property_detail'),
    # path('property/filter/<str:filter_type>/', views.property_filter, name='property_filter'),
    path('property/filter/', views.property_filter, name='property_filter_location'),
]