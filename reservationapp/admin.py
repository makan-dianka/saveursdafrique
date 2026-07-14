from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reference', 'customer_name', 'phone', 'email', 'people_count', 'reservation_date', 'message', 'status', 'created_at')

