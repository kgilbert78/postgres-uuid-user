from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student, Enrollment, Course
from .serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
       
    # queryset = Student.objects.all().only("student")
    # queryset = Enrollment.objects.defer("enrolled_in")
    # queryset = Enrollment.objects.defer("Course.student")

class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()

    # queryset = Enrollment.objects.only("course")
    # queryset = Enrollment.objects.defer("student")

    # queryset = Enrollment.objects.all()#.only("course").select_related("course")
    # queryset = Enrollment.objects.values_list('id', 'course')

    # queryset = Enrollment.objects.defer("final_grade") # this works but only on enrollment endpoint!

    # i want "enrolled_in" to only return courses and "enrollees" to only return students
    # queryset = Enrollment.objects.defer("enrolled_in")
    # queryset = Enrollment.objects.defer("Course.students")

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    
    # queryset = Course.objects.all().only("course")
    # queryset = Course.objects.all()#.only("course").select_related("course")
    # queryset = Enrollment.objects.defer("student")
