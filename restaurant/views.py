from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
def home(request):
    context = {}
    return render(request, "index.html", context)

class BookingView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()

class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

class MenusView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()