import datetime

from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.extras.widgets import SelectDateWidget
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from profapp.models import Exam, Student, SemesterSubject, Grade
from profapp.forms import GradeForm


class GradeListView(ListView):
    template_name = "profapp/grade/grade_list.djhtml"
    context_object_name = "grades"
    model = Grade
    
    
class GradeMixin(object):
    """ A mixin to do standard stuff.
    """
    context_object_name = "grade"

    def get_success_url(self):
        """ Redirect to grade list view.
        """
        url = reverse('grade_list')
        return url

class GradeCreateView(GradeMixin, CreateView):
    model = Grade
    form_class = GradeForm
    template_name = "profapp/grade/grade_form.djhtml"


class GradeUpdateView(GradeMixin, UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = "profapp/grade/grade_form.djhtml"
   

class GradeDeleteView(GradeMixin, DeleteView):
    model = Grade
    slug_field = "subject"
    template_name = "profapp/grade/grade_confirm_delete.djhtml"

       

