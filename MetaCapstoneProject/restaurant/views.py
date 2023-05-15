from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return HttpResponse('About page')

def book(request):
    return HttpResponse('Book page')

def menu(request):
    return HttpResponse('Menu page')

def display_menu_item(request):
    return HttpResponse('Menu item page')
