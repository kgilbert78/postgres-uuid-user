from rest_framework import viewsets
from .models import File
from .serializer import FileSerializer
from django.db.backends.postgresql.psycopg_any import NumericRange

class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def get_serializer_context(self):
        start_query = ""
        end_query = ""
        if self.request.query_params["start"]:
            start_query = self.request.query_params["start"]
        if self.request.query_params["end"]:
            end_query = self.request.query_params["end"]
        # if self.request.query_params:
        #     for param in self.request.query_params:
        #         print("param", param, self.request.query_params[param])
        #         # http://localhost:8000/file-dates/?start=1987-01-01&end=1987-12-31
        
        if start_query and end_query:
            print(f'search {start_query} to {end_query}')
            filtered_files = File.objects.filter(orig_date_start__range=(start_query, end_query))
            for file in filtered_files:
                print(file.name)
            return filtered_files


# https://www.austingrandt.com/writing/how-to-pass-query-parameters-to-serializers-in-django-rest-framework-drf/

# https://stackoverflow.com/questions/31038742/pass-request-context-to-serializer-from-viewset-in-django-rest-framework
                