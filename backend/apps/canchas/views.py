from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Cancha
from .serializers import CanchaSerializer

class CanchaList(ListAPIView):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer