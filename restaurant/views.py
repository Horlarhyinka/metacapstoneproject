from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu

# Create your views here.
def home(request):
    context = {}
    return render(request, "index.html", context)

class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()