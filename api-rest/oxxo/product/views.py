from django.shortcuts import render
from rest_framework import viewsets
from .models import Beer
from .serializers import BeerSerializer

# Create your views here.

class BeerViewSet(viewsets.ModelViewSet):
    serializer_class = BeerSerializer
    queryset = Beer.objects.all()
