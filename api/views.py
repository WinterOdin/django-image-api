from rest_framework import viewsets
from .serializers import PictureSerializer
from .models import Pictures
from .filters import PictureFilter


class PictureViewset(viewsets.ModelViewSet):
    serializer_class = PictureSerializer
    filterset_class = PictureFilter
    queryset = Pictures.objects.all()
