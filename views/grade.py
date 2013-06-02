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

    def get_context_data(self, **kwargs):
        stud = self.request.GET.get('stud')
        if stud:
	    if Grade.objects.filter(student=int(stud)):
                kwargs['student'] = Grade.objects.get(student=int(stud))

        return super(GradeListView, self).get_context_data(**kwargs)
    
    def get_queryset(self):
        stud = self.request.GET.get('stud')
        if stud and Grade.objects.filter(student=int(stud)):
            return Grade.objects.filter(student=int(stud))
        else:
            return super(GradeListView, self).get_queryset()
    
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

       

