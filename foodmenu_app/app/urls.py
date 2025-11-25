from django.contrib import admin
from django.urls import path
from . import views
app_name='app'
urlpatterns = [
    path('', views.index,name='index'),
    path("<int:id>/",views.detail,name='detail'),
    path("add/",views.create_item,name='Item_name'),
    path("update/<int:id>/",views.update,name="update")
]