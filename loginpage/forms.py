from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.lower().endswith("@byui.edu"):
            raise ValidationError("Email must end with @byui.edu")
        return email
