from django.db import models


class RestaurantInfo(models.Model):

    name = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    phone = models.CharField(
        max_length=30
    )

    email = models.EmailField(
        blank=True
    )

    address = models.TextField()

    google_map_url = models.URLField(
        blank=True
    )

    facebook = models.URLField(
        blank=True
    )

    instagram = models.URLField(
        blank=True
    )

    hero_image = models.ImageField(
        upload_to="restaurant/",
        blank=True
    )

    logo = models.ImageField(
        upload_to="restaurant/",
        blank=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurant"

    def __str__(self):
        return self.name



class ContactMessage(models.Model):

    name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    subject = models.CharField(
        max_length=255
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.subject