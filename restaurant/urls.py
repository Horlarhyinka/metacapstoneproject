from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/bookings/", views.BookingView.as_view(), name="bookings"),
    path("api/bookings/<int:id>", views.SingleBookingView.as_view(), name="booking"),
    path("api/menu-items/", views.MenusView.as_view(), name="menu_items"),
    path("api/menu-items/<int:id>", views.SingleMenuView.as_view(), name="menu")
]