from django.urls import path
from . import views

urlpatterns = [
    path("", views.store_view, name="store"),           
    path("login/", views.login_view, name="login"),     
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),  
    path("home/", views.home_view, name="home"),        
    path("create/", views.create_listing, name="create-listing"),
    path("dashboard/", views.user_dashboard, name="user-dashboard"),
    path("delete/<int:listing_id>/", views.delete_listing, name="delete-listing"),
    path("edit/<int:listing_id>/", views.edit_listing, name="edit-listing"),
    path("listing/<int:listing_id>/", views.listing_detail, name="listing-detail"),
    path("seller/<int:seller_id>/", views.seller_profile, name="seller-profile"),
    path("chat/", views.chat_view, name="chat"),
    path("chat/listing/<int:listing_id>/", views.conversation_view, name="conversation"),
    path("inbox/", views.inbox_view, name="inbox"),
]