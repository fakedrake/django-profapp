from django.forms import ModelForm

from profapp.models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
