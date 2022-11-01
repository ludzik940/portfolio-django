from django.shortcuts import render
from django.views.generic import ListView

from .models import Links

# Create your views here.

def home(request):
    links= Links.objects.all()
    return render(request, 'index.html', {'links' : links})

