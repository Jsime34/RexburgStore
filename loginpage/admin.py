from django.contrib import admin
from .models import Listing, Message

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'condition', 'seller', 'created_at')
    search_fields = ('title', 'description', 'category')
    list_filter = ('category', 'condition')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'listing', 'timestamp')
    search_fields = ('content',)
    list_filter = ('timestamp',)

admin.site.register(Listing, ListingAdmin)
admin.site.register(Message, MessageAdmin)
