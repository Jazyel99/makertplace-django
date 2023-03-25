from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item

def index(request):
  # catching items of logged user
  items = Item.objects.filter(created_by=request.user)
  
  return render(request, 'dashboard/index.html', {
    'items': items
  })
