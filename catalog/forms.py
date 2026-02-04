from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Product, Recommendation

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "product_type", "description", "ingredients", "price", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "product_type": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "ingredients": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ["full_name", "email", "category", "concerns", "recommended_products"]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "concerns": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "recommended_products": forms.SelectMultiple(attrs={"class": "form-control"}),
        }