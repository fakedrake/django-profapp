import datetime

from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.extras.widgets import SelectDateWidget
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from profapp.models import SemesterSubject
from profapp.forms import SemesterSubjectForm


class SubjectDetailView(DetailView):
    template_name = "profapp/subject/subject_details.djhtml"
    context_object_name = "subject"
    model = SemesterSubject
    slug_field = 'name'

class SubjectYearDetailView(DetailView):
    template_name = "profapp/subject/subject_year_details.djhtml"
    context_object_name = "subject_year"
    model = SemesterSubject
    slug_field = ('name','year')

class SubjectListView(ListView):
    template_name = "profapp/subject/subject_list.djhtml"
    context_object_name = "subjects"
    model = SemesterSubject
    
    def get_queryset(self):
	return SemesterSubject.objects.values('name').distinct()

class SubjectYearListView(ListView):
    template_name = "profapp/subject/subject_year_list.djhtml"
    context_object_name = "subjects_year"
    model = SemesterSubject
    slug_field = 'name'

    def get_queryset(self):
	
	return SemesterSubject.objects.filter()


class SemesterSubjectMixin(object):
    """ A mixin to do standard stuff.
    """
    context_object_name = "subject_year"

    def get_success_url(self):
        """ Redirect to subject_year view.
        """
        return reverse('subject_year_view', kwargs={ 'slug':str(self.object.name), 'pk':self.object.pk })

class SemesterSubjectCreateView(SemesterSubjectMixin, CreateView):
    model = SemesterSubject
    form_class = SemesterSubjectForm
    template_name = "profapp/subject/subject_form.djhtml"
    slug_field = ("name", "year")


class SemesterSubjectUpdateView(SemesterSubjectMixin, UpdateView):
    model = SemesterSubject
    form_class = SemesterSubjectForm
    template_name = "profapp/subject/subject_form.djhtml"
    slug_field = "name"

class SemesterSubjectDeleteView(DeleteView):
    model = SemesterSubject
    slug_field = "name"
    template_name = "profapp/subject/subject_confirm_delete.djhtml"
    success_url = reverse_lazy('subject_list')

