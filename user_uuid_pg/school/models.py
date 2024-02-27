import uuid
from django.db import models

class Student(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=30)
    # students = models.ManyToManyField(Student, through='Enrollment', through_fields=('course', 'student'))

    def __str__(self):
        return self.name        

class Enrollment(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    student = models.ForeignKey(Student, related_name='enrolled_in', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollees', on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    final_grade = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.student.name} in {self.course.name}"

    class Meta:
        unique_together = [['student', 'course']]