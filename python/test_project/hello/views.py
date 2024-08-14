from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def Chioma(request):
    return HttpResponse("Chioma is a good girl")

def Obinna(request):
    return HttpResponse("Obinna loves Chioma")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })