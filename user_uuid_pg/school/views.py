from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student, Enrollment, Course
from .serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    second_serializer = StudentSerializer(queryset, many=True)

    res_list = []

    for each_student in second_serializer.data:
        res_dict = {}
        # print(dict(each_student))
        student_dict = dict(each_student)
        for each_key in student_dict:
            # print(each_key)
            if each_key == "enrolled_in":
                # print(student_dict[each_key])
                # print(dict(student_dict[each_key][0]))
                enrollment_dict = dict(student_dict[each_key][0])
                # print(enrollment_dict)
                # {'id': 3, 'date_enrolled': '2023-12-01', 'final_grade': 'B', 'student': OrderedDict([('id', 3), ('name', 'Gilbert')]), 'course': OrderedDict([('id', 3), ('name', 'Science'), ('students', [3])])}

                # print(student_dict[each_key][0].keys())
                # odict_keys(['id', 'date_enrolled', 'final_grade', 'student', 'course'])
                enrollment_odict = student_dict[each_key][0]
                eo_dict = {}
                eo_keys = student_dict[each_key][0].keys()
                # print(enrollment_odict[eo_keys])
                for eokey in enrollment_odict:
                    # print(eokey, enrollment_odict[eokey])
                    # id 3
                    # date_enrolled 2023-12-01
                    # final_grade B
                    # student OrderedDict([('id', 3), ('name', 'Gilbert')])
                    # course OrderedDict([('id', 3), ('name', 'Science'), ('students', [3])])
                    if eokey != 'student':
                        # print(eokey, enrollment_odict[eokey])
                        eo_dict[eokey] = enrollment_odict[eokey]
                res_dict["enrolled_in"] = eo_dict
            else:
                res_dict[each_key] = student_dict[each_key]
            # print("res_dict", res_dict)
            res_list.append(res_dict)
    
    print("RES LIST", res_list)

    # prints what i want to return in the get_queryset when def (next 2 lines) commented out

    # # def get_queryset(self, res_list=res_list):
    # #     return res_list
    

    # def get_queryset(self, serializer_class=serializer_class):
    #     students = Student.objects.all()
    #     # print("students", students)
    #     print(repr(serializer_class))
    #     return students
    
    
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
