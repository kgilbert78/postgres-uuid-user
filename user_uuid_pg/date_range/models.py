from django.db import models
from django.contrib.postgres.fields import DateRangeField

# Create your models here.
class File(models.Model):
    name=models.CharField(max_length=150)
    orig_doc_date = DateRangeField() # from postgres import not models

    def __str__(self):
        return self.name