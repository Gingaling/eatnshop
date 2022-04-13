# grocery/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # GET localhost:8000/grocery
    # POST localhost:8000/grocery

    path('grocery/', views.GroceryList.as_view(), name='grocery_list'),

    # PUT localhost:8000/grocery/:id
    # DELETE localhost:8000/grocery/:id

    path('grocery/<int:pk>',
         views.GroceryDetail.as_view(), name='grocery_detail'),

 
]
