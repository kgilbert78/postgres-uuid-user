from rest_framework import viewsets
from .models import File
from .serializer import FileSerializer
from django.db.backends.postgresql.psycopg_any import NumericRange

class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer

    def get_queryset(self):
        queryset = File.objects.all()

        start_query = self.request.query_params.get("start")
        end_query = self.request.query_params.get("end")

        if start_query is not None:
            queryset = File.objects.filter(orig_date_start__range=(start_query, end_query))

        return queryset


# https://medium.com/django-rest-for-not-beginners/generic-viewsets-serializer-context-and-hooks-1aa0000bc71d