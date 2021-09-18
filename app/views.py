from django.shortcuts import render
from django.shortcuts import get_list_or_404, render, redirect
from django.views.generic.list import ListView

from app.models import Problem

# Create your views here.
def top(request):
    return render(request, 'app/top.html')

def submit(request):
    return render(request, 'app/submit.html')