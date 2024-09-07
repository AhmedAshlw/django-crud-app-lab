from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("flights/", views.flight_index, name="flight-index"),
    path("flights/<int:flight_id>/", views.flight_detail, name="flight-detail"),
    path("flights/create/", views.FlightCreate.as_view(), name="flight-create"),
    path(
        "flights/<int:pk>/update/", views.FlightUpdate.as_view(), name="flight-update"
    ),
    path(
        "flights/<int:pk>/delete/", views.FlightDelete.as_view(), name="flight-delete"
    ),
    path("accounts/signup/", views.signup, name="signup"),
]
