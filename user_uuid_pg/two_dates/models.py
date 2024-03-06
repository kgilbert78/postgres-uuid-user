from django.db import models

# Create your models here.
class File(models.Model):
    name=models.CharField(max_length=150)
    orig_date_start = models.DateField()
    orig_date_end = models.DateField()

    def __str__(self):
        return self.name