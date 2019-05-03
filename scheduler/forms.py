from django.forms import ModelForm
from .models import Course, Instructor

class CourseForm(ModelForm):
    class Meta: 
        model = Course
        fields = ['class_name']


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = ['i_name']

class CourseInstructorForm(ModelForm):
    class Meta:
        model = Course
        fields = ['instructor']
