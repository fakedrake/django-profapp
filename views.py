# geia
import datetime

from django import forms
from django.core.urlresolvers import reverse_lazy
from django.forms.extras.widgets import SelectDateWidget
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from profapp.models import Student
from profapp.forms import StudentForm

class SqlPresenterMixin(object):
    """ Provide the sql query to the context.
    """

    def get_context_data(self, **kwargs):
        context = super(SqlPresenterMixin, self).get_context_data(**kwargs)

        context['sqlquery'] = str(self.get_queryset().query)
        return context

class StudentDetailView(SqlPresenterMixin, DetailView):
    template_name = "profapp/student_details.html"
    context_object_name = "student"
    model = Student
    slug_field = 'am'



class StudentListView(SqlPresenterMixin, ListView):
    template_name = "profapp/student_list.html"
    context_object_name = "students"
    model = Student


class StudentMixin(object):
    """ A mixin to do standard stuff.
    """
    context_object_name = "student"

    def get_success_url(self):
        """ Redirect to student view.
        """
        return "/students/%s/" % str(self.object.am)


class StudentCreateView(SqlPresenterMixin, StudentMixin, CreateView):
    form_class = StudentForm
    template_name = "profapp/student_form.html"
    slug_field = "am"

class StudentUpdateView(SqlPresenterMixin, StudentMixin, UpdateView):
    form_class = StudentForm
    template_name = "profapp/student_form.html"
    slug_field = "am"

class StudentDeleteView(SqlPresenterMixin, DeleteView):
    model = Student
    slug_field = "am"
    success_url = reverse_lazy('student-list')
