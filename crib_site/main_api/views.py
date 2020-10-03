from rest_framework import generics
from .models import Crib
from .serializer import CribSerializer

class CribList(generics.ListCreateAPIView):
    queryset = Crib.objects.all()
    serializer_class = CribSerializer

class CribDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crib.objects.all()
    serializer_class = CribSerializer
