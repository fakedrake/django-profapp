import datetime

from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.extras.widgets import SelectDateWidget
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from profapp.models import Student, SemesterSubject
from profapp.forms import StudentForm


class SqlPresenterMixin(object):
    """ Provide the sql query to the context.
    """

    def get_context_data(self, **kwargs):
        context = super(SqlPresenterMixin, self).get_context_data(**kwargs)

        context['sqlquery'] = str(self.get_queryset().query)
        return context

# about Student

class StudentDetailView(SqlPresenterMixin, DetailView):
    template_name = "profapp/student_details.djhtml"
    context_object_name = "student"
    model = Student
    slug_field = 'am'


class StudentListView(SqlPresenterMixin, ListView):
    template_name = "profapp/student_list.djhtml"
    context_object_name = "students"
    model = Student


class StudentMixin(object):
    """ A mixin to do standard stuff.
    """
    context_object_name = "student"

    def get_success_url(self):
        """ Redirect to student view.
        """
        return reverse('student_view', kwargs={ 'slug':str(self.object.am)})


class StudentCreateView(SqlPresenterMixin, StudentMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "profapp/student_form.djhtml"
    slug_field = "am"


class StudentUpdateView(SqlPresenterMixin, StudentMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "profapp/student_form.djhtml"
    slug_field = "am"

class StudentDeleteView(SqlPresenterMixin, DeleteView):
    model = Student
    slug_field = "am"
    template_name = "profapp/student_confirm_delete.djhtml"
    success_url = reverse_lazy('student_list')

# about SemesterSubject
