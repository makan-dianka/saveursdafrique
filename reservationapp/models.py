from django.db import models


class Reservation(models.Model):

    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

    STATUS = [
        (PENDING, "En attente"),
        (CONFIRMED, "Confirmée"),
        (CANCELLED, "Annulée"),
    ]
    reference = models.CharField(max_length=100, unique=True, null=True)
    customer_name = models.CharField(
        max_length=255
    )

    phone = models.CharField(
        max_length=30
    )

    email = models.EmailField()

    people_count = models.PositiveIntegerField()

    reservation_date = models.DateTimeField()

    message = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default=PENDING
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-reservation_date"]

    def __str__(self):
        return (
            f"{self.customer_name}"
            f" - "
            f"{self.reservation_date}"
        )