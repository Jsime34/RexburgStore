from django.urls import path
from . import views

urlpatterns = [
    path("", views.store_view, name="store"),           # Store homepage
    path("login/", views.login_view, name="login"),     # Login route
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),  # Logout route
    path("home/", views.home_view, name="home"),        # Optional dashboard
    path("create/", views.create_listing, name="create-listing"),
 #Create listing
]
