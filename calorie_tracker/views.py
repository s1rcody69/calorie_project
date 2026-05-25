from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import FoodItem
from .forms import FoodItemForm

def index(request):
    """Display all food items for today and handle adding new ones."""
    today = timezone.now().date()
    items = FoodItem.objects.filter(date_added=today)
    total = sum(item.calories for item in items)
    form = FoodItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'calorie_tracker/index.html', {'items': items, 'total': total, 'form': form})

def edit(request, pk):
    """Edit an existing food item."""
    item = get_object_or_404(FoodItem, pk=pk)
    form = FoodItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'calorie_tracker/edit.html', {'form': form, 'item': item})

def delete(request, pk):
    """Delete a food item."""
    item = get_object_or_404(FoodItem, pk=pk)
    if request.method == 'POST':
        item.delete()
    return redirect('index')

def reset(request):
    """Delete all food items for today."""
    if request.method == 'POST':
        FoodItem.objects.filter(date_added=timezone.now().date()).delete()
    return redirect('index')