from django.contrib import admin
from django.urls import path
from . import views
app_name='app'
urlpatterns = [
    path('', views.index,name='index'),
    path("item/",views.item,name='item'),
    path("<int:id>/",views.detail,name='detail'),
]