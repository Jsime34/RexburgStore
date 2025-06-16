from django.urls import path
from . import views

urlpatterns = [
    path("", views.store_view, name="store"),                             # Store homepage
    path("login/", views.login_view, name="login"),                       # Login
    path("signup/", views.signup_view, name="signup"),                    # Signup
    path("logout/", views.logout_view, name="logout"),                    # Logout
    path("home/", views.home_view, name="home"),                          # Optional dashboard/homepage
    path("create/", views.create_listing, name="create-listing"),         # Create a new listing
    path("dashboard/", views.user_dashboard, name="user-dashboard"),      # User dashboard
    path("edit-profile/", views.edit_profile, name="edit-profile"),       # Edit profile
    path("listing/<int:listing_id>/", views.listing_detail, name="listing-detail"),              # View a listing
    path("listing/<int:listing_id>/edit/", views.edit_listing, name="edit-listing"),             # Edit a listing
    path("listing/<int:listing_id>/delete/", views.delete_listing, name="delete-listing"),       # Delete a listing
    path("seller/<int:seller_id>/", views.seller_profile, name="seller-profile"),                # Seller profile page
    path("chat/", views.chat_view, name="chat"),                                                  # Chat page
    path("inbox/", views.inbox_view, name="inbox"),                                               # Inbox view
    path("conversation/<int:listing_id>/", views.conversation_view, name="conversation"),         # Conversation per listing
]
