from django.shortcuts import render
from item.models import Category, Item

# Create your views here.
def index(request):
    #get first 6 unsold items
    items = Item.objects.filter(is_sold = False)[0:6]
    #get categories
    categories = Category.objects.all()

    context = {
        'categories' : categories,
        'items' : items
    }
    return render (request, 'crudapp/index.html', context)

def contact(request):
    return render (request, 'crudapp/contact.html')