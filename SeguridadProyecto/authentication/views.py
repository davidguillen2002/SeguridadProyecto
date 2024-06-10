# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Especifica el backend explícitamente
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("home")
        else:
            # Invalid login
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")
