from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ListingForm


def loginpage(response):
    return render(response, "loginpage/loginpage.html", {})

@login_required
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user
            listing.save()
            return redirect("store")  # or use a detail view later
    else:
        form = ListingForm()
    return render(request, "loginpage/create_listing.html", {"form": form})