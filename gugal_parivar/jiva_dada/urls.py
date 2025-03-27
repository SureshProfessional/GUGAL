from django.contrib import admin
from django.urls import path,include
from jiva_dada import views


urlpatterns = [
    path('',views.index,name="index"),
    path('addname',views.addname,name="addname"),
]