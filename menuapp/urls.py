from django.urls import path
from . import views

app_name = 'menuapp'
urlpatterns = [
    path('menu/', views.menu_view, name="menu"),
    path("create/", views.product_create_view, name="create"),
]