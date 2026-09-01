from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def hello_world(r):
    return HttpResponse("<h1>Hello world!</h1>")

def my_name(r):
    name = "Yrysgul"

    return HttpResponse(f"<h2>Hello,</h2><h1>{name}</h1>")

def say_name(r, name):
    return HttpResponse(f"<h2>Hello,</h2><h1>{name}</h1>")