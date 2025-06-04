from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginpage, name= ("login Page")),
    path("listings/new/", views.create_listing, name="create_listing")
]


# testing

