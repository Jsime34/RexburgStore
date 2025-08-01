from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm 
from .forms import ListingForm
from .models import Listing


def store_view(request):
    return render(request, "loginpage/loginpage.html")  # store main page


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("store")  # redirect to store
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "loginpage/login.html")


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now log in.")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "loginpage/signup.html", {"form": form})


@login_required
def home_view(request):
    return render(request, "loginpage/home.html")  # optional


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

@login_required
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user
            listing.save()
            messages.success(request, "Listing created successfully!")
            return redirect("create-listing")  # stays on page
    else:
        form = ListingForm()
    return render(request, "loginpage/create_listing.html", {"form": form})


