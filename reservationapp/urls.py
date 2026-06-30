from django.urls import path
from . import views

app_name = 'reservationapp'

urlpatterns = [
    path("new/", views.reservation_create_view, name="create"),
    path("list/", views.reservation_list_view, name="list"),

    path("<int:pk>/<str:status>/", views.reservation_update_status, name="update_status"),
]