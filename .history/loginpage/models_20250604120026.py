from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    CATEGORY_CHOICES = [
        ("electronics", "Electronics"),
        ("furniture", "Furniture"),
        ("books", "Books"),
        ("clothing", "Clothing"),
        ("other", "Other"),
    ]

    CONDITION_CHOICES = [
        ("new", "New"),
        ("like_new", "Like New"),
        ("used", "Used"),
        ("for_parts", "For Parts"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default="used")
    location = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="listing_images/", blank=True, null=True)  # ✅ New field
    is_active = models.BooleanField(default=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} - ${self.price}"
