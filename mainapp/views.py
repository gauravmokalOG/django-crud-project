from django.shortcuts import render, get_object_or_404, redirect
from .models import Item

def index(request):
    items = Item.objects.all()
    return render(request, 'mainapp/index.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'mainapp/item_detail.html', {'item': item})

def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        Item.objects.create(name=name, description=description, quantity=quantity)
        return redirect('index')
    return render(request, 'mainapp/item_form.html')

def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        item.quantity = request.POST.get('quantity')
        item.save()
        return redirect('index')
    return render(request, 'mainapp/item_form.html', {'item': item})

def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'mainapp/item_confirm_delete.html', {'item': item})
