from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "customer_name",
            "phone",
            "email",
            "people_count",
            "reservation_date",
            "message",
        ]

        CHOICES = [(i, f"{i} personne{'s' if i > 1 else ''}") for i in range(1, 11)]

        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            'people_count': forms.Select(choices=CHOICES, attrs={'class': 'form-control mb-3'}),
            "reservation_date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local"
                }
            ),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }


        labels = {
            'customer_name': 'Nom',
            'phone': 'Téléphone',
            'email': 'Adresse email',
            'people_count': 'Nombre de personne',
            'reservation_date': 'Date de réservation',
            'message': 'Message',
        }