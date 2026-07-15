from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm
from myproject import tools
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# CREATE RESERVATION (client)
def reservation_create_view(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.reference = tools.generate_reference('RSV', Reservation)
            reservation.save()

            maildata = {
                "username" : reservation.customer_name,
                "usermail" : reservation.email,
                "mailsubject" : "Confirmation de votre reservation",
                "html_file" : "email_templates/reservation.html",
                "txt_file" : "email_templates/reservation.txt",
                "reference" : reservation.reference,
                "message" : reservation.message
            }
            tools.sendmail(**maildata)
            messages.success(request, f"Votre réservation a bien été prise en compte. Votre code de reservation est : {reservation.reference}")
            return render(request, 'reservationapp/reservation_success.html')
    else:
        form = ReservationForm()

    return render(request, "reservationapp/reservation_form.html", {"form": form})


# LIST (admin / restaurant)
@login_required(login_url='accounts:login')
def reservation_list_view(request):
    reservations = Reservation.objects.all()
    return render(request, "reservationapp/reservation_list.html", {"reservations": reservations})


# UPDATE STATUS (confirm / cancel)
@login_required(login_url='accounts:login')
def reservation_update_status(request, pk, status):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.status = status
    reservation.save()
    return redirect("reservationapp:list")