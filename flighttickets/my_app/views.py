from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Flight


class Home(LoginView):
    template_name = "home.html"


def about(request):
    return render(request, "about.html")


@login_required
def flight_index(request):
    flights = Flight.objects.filter(user=request.user)
    return render(request, "flights/index.html", {"flights": flights})


@login_required
def flight_detail(request, flight_id):
    flights = Flight.objects.get(id=flight_id)
    return render(request, "flights/detail.html", {"flights": flights})


class FlightCreate(LoginRequiredMixin, CreateView):
    model = Flight
    fields = "__all__"
    success_url = "/flights/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FlightUpdate(LoginRequiredMixin, UpdateView):
    model = Flight
    fields = ["sourcePlace", "destinationPlace", "description"]


class FlightDelete(LoginRequiredMixin, DeleteView):
    model = Flight
    success_url = "/flights/"


def signup(request):
    error_message = ""
    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect("cat-index")
        else:
            error_message = "Invalid sign up - try again"

    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)
