import datetime

from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.extras.widgets import SelectDateWidget
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from profapp.models import Student, SemesterSubject
from profapp.forms import StudentForm


class StudentDetailView(DetailView):
    template_name = "profapp/student/student_details.djhtml"
    context_object_name = "student"
    model = Student
    slug_field = 'am'


class StudentListView(ListView):
    template_name = "profapp/student/student_list.djhtml"
    context_object_name = "students"
    model = Student
    
    def get_queryset(self):
	subject = self.request.GET.get("subj")
	if subject:
	    obj = SemesterSubject.objects.get(pk=subject)
	    return obj.students.all()
	else:
	    return super(StudentListView, self).get_queryset()
  	

class StudentMixin(object):
    """ A mixin to do standard stuff.
    """
    context_object_name = "student"

    def get_success_url(self):
        """ Redirect to student view.
        """
        return reverse('student_view', kwargs={ 'slug':str(self.object.am)})


class StudentCreateView(StudentMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "profapp/student/student_form.djhtml"
    slug_field = "am"


class StudentUpdateView(StudentMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "profapp/student/student_form.djhtml"
    slug_field = "am"

class StudentDeleteView(DeleteView):
    model = Student
    slug_field = "am"
    template_name = "profapp/student/student_confirm_delete.djhtml"
    success_url = reverse_lazy('student_list')

