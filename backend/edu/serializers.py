from rest_framework.serializers import ModelSerializer
from .models import Teacher, Course, Student


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializer(ModelSerializer):
    teacher = TeacherSerializer
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(ModelSerializer):
    courses = CourseSerializer
    class Meta:
        model = Student
        fields = '__all__'