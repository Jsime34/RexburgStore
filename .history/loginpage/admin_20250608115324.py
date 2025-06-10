from django.contrib import admin
from .models import Listing, Message

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'condition', 'seller', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('category', 'condition', 'created_at')
    ordering = ('-created_at',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('listing', 'sender', 'receiver', 'timestamp')
    search_fields = ('content',)
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
