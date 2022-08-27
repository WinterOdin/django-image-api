from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PictureSerializer
from .models import Pictures
# Create your views here.

class PictureViewset(viewsets.ModelViewSet):

    serializer_class = PictureSerializer
    queryset = Pictures.objects.all()
