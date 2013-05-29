from django import forms
from django.forms import ModelForm

from profapp.models import Student, SemesterSubject
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput

class StudentForm(ModelForm):

    date_enrolled = forms.DateField(widget=BootstrapDateInput(),)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'am', 'date_enrolled', 'semester', 'undergraduate']


class SemesterSubjectForm(ModelForm):

    class Meta:
	model = SemesterSubject
