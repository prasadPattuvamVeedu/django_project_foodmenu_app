from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
def index(request):
    item_list=Item.objects.all()
    context={"item_list":item_list}
    return render(request,"app/index.html",context)
def detail(request,id):
    list1=Item.objects.get(id=id)
    context={"list1":list1}
    return render(request,"app/list.html",context)
def item(request):
    return HttpResponse("<H1>item is not Found<H1>")
# Create your views here.
