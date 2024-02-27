from rest_framework import serializers
from .models import Student, Course, Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'date_enrolled', 'final_grade']
        # exclude = ['student']
        depth = 2

class StudentSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/serializers/#specifying-fields-explicitly
    # course_list = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # print("course_list", course_list)
    # course_list = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='course_list'
    #  )
    class Meta:
        model = Student
        # fields = ['id', 'name', 'course_list']
        fields = ['id', 'name', 'enrolled_in']
        depth = 2

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'enrollees']
        depth = 2
