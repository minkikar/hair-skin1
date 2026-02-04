from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from .forms import LoginForm, ProductForm, RecommendationForm
from .models import Product, Recommendation

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if user:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Invalid username or password.")
    return render(request, "catalog/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard(request):
    product_count = Product.objects.count()
    recommendation_count = Recommendation.objects.count()
    top_products = (
        Product.objects.annotate(reco_count=Count("recommendations"))
        .filter(reco_count__gt=0)
        .order_by("-reco_count", "name")[:5]
    )
    context = {
        "product_count": product_count,
        "recommendation_count": recommendation_count,
        "top_products": top_products,
    }
    return render(request, "catalog/dashboard.html", context)

@login_required
def product_list(request):
    products = Product.objects.order_by("name")
    return render(request, "catalog/product_list.html", {"products": products})

@login_required
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Product added successfully.")
        return redirect("product_list")
    return render(request, "catalog/product_form.html", {"form": form, "title": "Add"})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Product updated successfully.")
        return redirect("product_list")
    return render(request, "catalog/product_form.html", {"form": form, "title": "Edit", "product": product})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully.")
        return redirect("product_list")
    return render(request, "catalog/product_confirm_delete.html", {"product": product})

@login_required
def recommendation_list(request):
    recommendations = Recommendation.objects.prefetch_related("recommended_products").order_by("-created_at")
    popular_products = (
        Product.objects.annotate(reco_count=Count("recommendations"))
        .filter(reco_count__gt=0)
        .order_by("-reco_count", "name")
    )
    context = {
        "recommendations": recommendations,
        "popular_products": popular_products,
    }
    return render(request, "catalog/recommendation_list.html", context)

@login_required
def recommendation_create(request):
    form = RecommendationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Recommendation saved successfully.")
        return redirect("recommendation_list")
    return render(request, "catalog/recommendation_form.html", {"form": form, "title": "New"})