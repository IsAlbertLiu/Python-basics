from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello World")


def new(requset):
    return HttpResponse('New Products')


def info(request):
    return HttpResponse("My First Django Demo")
