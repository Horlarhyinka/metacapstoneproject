from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'tables', views.BookingViewSet, basename="booking")

urlpatterns = [
    path("", views.home, name="home"),
    path("bookings/", include(router.urls))
]