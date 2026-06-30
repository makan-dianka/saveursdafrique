from django import forms
from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "category",
            "name",
            "description",
            "price",
            "image",
            "is_available",
        ]
        widgets = {
            "category": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "is_available": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }



        labels = {
            'category': 'Catégorie',
            'name': 'Nom',
            'price': 'Prix',
            'people_count': 'Nombre de personne',
            'is_available': 'Disponible',
        }


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ["image"]
        widgets = {
            "image": forms.ClearableFileInput(attrs={"class": "form-control"})
        }