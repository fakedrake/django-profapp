import datetime

from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.extras.widgets import SelectDateWidget
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from profapp.models import Exam, SemesterSubject
from profapp.forms import ExamForm


class ExamListView(ListView):
    template_name = "profapp/exam/exam_list.djhtml"
    context_object_name = "exams"
    model = Exam

    def get_context_data(self, **kwargs):       
        kwargs['subject'] = SemesterSubject.objects.get(pk=int(self.request.GET.get('subj')))
	return super(ExamListView, self).get_context_data(**kwargs)		

    def get_queryset(self):
	c = Exam.objects.filter(subject=int(self.request.GET.get('subj')))	
	return c    

class ExamMixin(object):
    """ A mixin to do standard stuff.
    """
    context_object_name = "exam"

    def get_success_url(self):
        """ Redirect to exam view.
        """
        url = "%s?subj=%s" % (reverse('exam_view'),str(self.object.subject.pk)) 
	return url

class ExamCreateView(ExamMixin, CreateView):
    model = Exam
    form_class = ExamForm
    template_name = "profapp/exam/exam_form.djhtml"
    slug_field = "subject"


class ExamUpdateView(ExamMixin, UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = "profapp/exam/exam_form.djhtml"
    slug_field = "subject"

class ExamDeleteView(DeleteView):
    model = Exam
    slug_field = "subject"
    template_name = "profapp/exam/exam_confirm_delete.djhtml"

    def get_success_url(self):
	url = "%s?subj=%s" % (reverse('exam_view'),str(self.object.subject.pk))
	return url
