from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm 
from .forms import ListingForm
from .models import Listing
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


def store_view(request):
    listings = Listing.objects.all()
    categories = Listing.objects.values_list('category', flat=True).distinct()

    selected_category = request.GET.get('category')
    if selected_category:
        listings = listings.filter(category=selected_category)

    return render(request, "loginpage/loginpage.html", {
        "listings": listings,
        "categories": categories,
        "selected_category": selected_category,
    })


def login_view(request):
    show_alert = request.GET.get("auth_required") == "true"

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("store")  # redirect to store
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "loginpage/login.html", {"show_alert": show_alert})



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

@login_required(login_url='login')
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user
            listing.save()
            messages.success(request, "Listing created successfully!")
            return redirect("create-listing") 
    else:
        form = ListingForm()
    return render(request, "loginpage/create_listing.html", {"form": form})

@login_required
def user_dashboard(request):
    user = request.user
    user_listings = Listing.objects.filter(seller=user)

    context = {
        "user": user,
        "listings": user_listings,
    }
    return render(request, "loginpage/dashboard.html", context)

@login_required
def delete_listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id, seller=request.user)
    if request.method == "POST":
        listing.delete()
        messages.success(request, "Listing deleted.")
    return redirect("user-dashboard")


@login_required
def edit_listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id, seller=request.user)

    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request, "Listing updated successfully!")
            return redirect("user-dashboard")
    else:
        form = ListingForm(instance=listing)

    return render(request, "loginpage/edit_listing.html", {"form": form, "listing": listing})

def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return render(request, "loginpage/listing_detail.html", {"listing": listing})

def seller_profile(request, seller_id):
    seller = get_object_or_404(User, id=seller_id)
    listings = Listing.objects.filter(seller=seller)

    return render(request, "loginpage/seller_profile.html", {
        "seller": seller,
        "listings": listings
    })

from django.contrib.auth.decorators import login_required

@login_required
def chat_view(request):
    return render(request, "loginpage/chat.html", {"username": request.user.username})


