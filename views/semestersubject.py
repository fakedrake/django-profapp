import datetime

from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.extras.widgets import SelectDateWidget
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from profapp.models import SemesterSubject, Exam, Grade
from profapp.forms import SemesterSubjectForm


class SubjectYearDetailView(DetailView):
    template_name = "profapp/subject/subject_year_details.djhtml"
    context_object_name = "subject_year"
    model = SemesterSubject

    def get_context_data(self, **kwargs):
        kwargs['exam_count'] = len(Exam.objects.filter(subject=self.object.pk))
	kwargs['student_count'] = len(self.object.students.all())
	kwargs['grade_count'] = 0
	for e in Exam.objects.filter(subject=self.object.pk):
		kwargs['grade_count'] += len(Grade.objects.filter(exam=e.pk))

	return super(SubjectYearDetailView, self).get_context_data(**kwargs)


class SubjectListView(ListView):
    """
    List all subjects once. A subject may appear with the same name
    for amny years.
    """


    template_name = "profapp/subject/subject_list.djhtml"
    context_object_name = "subjects"
    model = SemesterSubject

    def get_queryset(self):
	return SemesterSubject.objects.values('name').distinct()

class SubjectYearListView(ListView):
    """
    Show all the years of a subject.
    """

    template_name = "profapp/subject/subject_year_list.djhtml"
    context_object_name = "subjects_year"
    model = SemesterSubject
    slug_field = 'name'

    def get_queryset(self):
     	subj = self.kwargs['slug']
        return SemesterSubject.objects.filter(name=subj).order_by('-year')


class SemesterSubjectMixin(object):
    """ A mixin to do standard stuff.
    """
    context_object_name = "subject_year"

    def get_success_url(self):
        """ Redirect to subject_year view.
        """
        return reverse('subject_year_view', kwargs={ 'pk': self.object.pk })

class SemesterSubjectCreateView(SemesterSubjectMixin, CreateView):
    model = SemesterSubject
    form_class = SemesterSubjectForm
    template_name = "profapp/subject/subject_form.djhtml"
    slug_field = "name"


class SemesterSubjectUpdateView(SemesterSubjectMixin, UpdateView):
    model = SemesterSubject
    form_class = SemesterSubjectForm
    template_name = "profapp/subject/subject_form.djhtml"
    slug_field = "name"

class SemesterSubjectDeleteView(DeleteView):
    model = SemesterSubject
    slug_field = ("name","year")
    template_name = "profapp/subject/subject_confirm_delete.djhtml"
    def get_success_url(self):

	return reverse('subject_year_list', kwargs={ 'slug':str(self.object.name) })
