from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, EnrollmentViewSet

router = DefaultRouter()

router.register(r"students", StudentViewSet, basename="students")
router.register(r"enrollment", EnrollmentViewSet, basename="enrollment")
router.register(r"courses", CourseViewSet, basename="courses")

urlpatterns = [
    path('api/', include(router.urls)),
]