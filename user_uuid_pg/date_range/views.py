from rest_framework import viewsets
from .models import File
from .serializer import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()