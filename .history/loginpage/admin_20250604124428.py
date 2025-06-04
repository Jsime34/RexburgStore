from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "condition", "category", "created_at", "seller")
    list_filter = ("category", "condition", "created_at")
    search_fields = ("title", "description", "seller__username")
