from rest_framework import generics, permissions, serializers
from .models import Slot
from .serializers import SlotSerializer

# Create your views here.

class SlotListView(generics.ListAPIView):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
