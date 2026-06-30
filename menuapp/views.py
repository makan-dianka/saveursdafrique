from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import ProductForm
from django.db.models import Prefetch

def menu_view(request):

    available_products = Product.objects.filter(
        is_available=True
    ).order_by("name")

    categories = (
        Category.objects
        .filter(
            is_active=True,
            products__is_available=True
        )
        .distinct()
        .order_by("order")
        .prefetch_related(
            Prefetch(
                "products",
                queryset=available_products
            )
        )
    )

    return render(
        request,
        "menuapp/menu.html",
        {
            "categories": categories
        }
    )


@login_required(login_url='accounts:login')
def product_create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("menuapp:menu")
    else:
        form = ProductForm()

    return render(request, "menuapp/product_form.html", {"form": form})
