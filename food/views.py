from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.template import loader

def index(request):                                  ##http response for /food/
    list=Item.objects.all()                          ##get the data from database
    context={
        'list':list}                                 ##what to pass in template 
    return render(request,'food/index.html',context)
def detail(request,item_id):                         ##http response for food/1/
    item=Item.objects.get(pk=item_id)                ##if matches with the primary id then renders the template
    context={
        'item':item,
    }
    return render(request,'food/detail.html',context)
def item(request):                                   ##http response for food/item
    return HttpResponse("<h1>Burrito and queso</h1>")

def create_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form})

    