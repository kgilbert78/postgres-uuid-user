from rest_framework import viewsets
from .models import File
from .serializer import FileSerializer
from django.db.backends.postgresql.psycopg_any import NumericRange

class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def get_serializer_context(self):
        start_date = ""
        end_date = ""
        if self.request.query_params["start"]:
            start_date = self.request.query_params["start"]
        if self.request.query_params["end"]:
            end_date = self.request.query_params["end"]
        # if self.request.query_params:
        #     for param in self.request.query_params:
        #         print("param", param, self.request.query_params[param])
        #         # http://localhost:8000/files/?start=01-01-1987&end=12-31-1987
        
        if start_date and end_date:
            # print(f'search {start_date} to {end_date}')
            filtered_files = File.objects.filter(orig_doc_date__contains=NumericRange(start_date, end_date)) # contains is wrong for what i want it to return
            for file in filtered_files:
                print(file.name)
            return filtered_files


# https://www.austingrandt.com/writing/how-to-pass-query-parameters-to-serializers-in-django-rest-framework-drf/

# https://stackoverflow.com/questions/31038742/pass-request-context-to-serializer-from-viewset-in-django-rest-framework
                