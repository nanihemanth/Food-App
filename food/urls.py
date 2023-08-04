from django.urls import path
from . import views

app_name='food'  ##namespacing to avoid confusions

urlpatterns = [
    path("", views.index,name='index'), ##food/
    path("<int:item_id>/", views.detail,name='detail'), ##food/1,food/2,food/3
    path("item", views.item,name='item'), #food/item
    path("add",views.create_item,name='create_item') #food/add/
]
