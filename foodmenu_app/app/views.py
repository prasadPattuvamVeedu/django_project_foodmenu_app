from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Itemform
from .models import Item
def index(request):
    item_list=Item.objects.all()
    context={"item_list":item_list}
    return render(request,"app/index.html",context)
def detail(request,id):
    list1=Item.objects.get(id=id)
    context={"list1":list1}
    return render(request,"app/list.html",context)
def create_item(request):
    form=Itemform(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect("app:index")
    context={'form':form}
    return render(request,"app/form_add.html",context)

def  update(request,id):
    lists=Item.objects.get(id=id)
    form=Itemform(request.POST or None,instance=lists)
    if request.method == "POST":
     if form.is_valid():
        form.save()
        return redirect("app:index")
    context={"form":form}
    return render(request,"app/form_add.html",context)