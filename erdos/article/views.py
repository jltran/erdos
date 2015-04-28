from django.shortcuts import render

#Rango Stuff
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello World")