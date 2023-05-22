from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def registarse(request):
    return HttpResponse("Bienvenidos")

def nuevousuario(request):
    return HttpResponse("hello")