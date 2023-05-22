from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request,email):
    return HttpResponse("Bienvenidos")

def hello(request):
    return HttpResponse("hello")