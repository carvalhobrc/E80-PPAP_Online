from django import forms
from django.contrib.auth.models import User
from authentication.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
        ]

class EmbracoUserForm(forms.ModelForm):
    class Meta:
        model = EmbracoProfile
        fields = [
            "department",
            "jobTitle",
            "phoneNumber",
        ]

class SupplierUserForm(forms.ModelForm):
    class Meta:
        model = SupplierProfile
        fields = [
            "user",
        ]
