from django.shortcuts import render, redirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse("login"))
    return render(request, "users/index.html")
    

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password')
             user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    else:
            form = AuthenticationForm()
    return render(request, "users/login.html", {
                "form": form
            })

   # return render(request, "users/login.html")

#Logout View
def logout_view(request):
    logout(request)
    return redirect(reverse('login'),  {
        "message": "Logged Out"
    })
  
#Register view
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
            form = RegisterForm()
    return render(request, "users/register.html", {
            "form":form
        })