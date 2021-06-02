from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

class HomeView(TemplateView):
    template_name = "index.html"

def register(request):
    if request.method=="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            messages.info(request, f"You are Logged in as: {username}")
            return redirect('/')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")


    form= UserCreationForm
    return render(request,"register.html",{"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')

def login_request(request):
    logout(request)
    if request.method=="POST":
        form=AuthenticationForm(request,data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are Logged in as: {username}")
                return redirect('/')
            else:
                messages.error(request,"Invalid Username or Password 1")
        else:
            messages.error(request,"Invalid Username or Password")

    form = AuthenticationForm()
    return render(request, 'login.html',{"form":form})