import datetime

from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.extras.widgets import SelectDateWidget
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from profapp.models import Exam, Student, SemesterSubject, Grade
from profapp.forms import GradeForm
from profapp.views.sorter import Sorter


class GradeListView(ListView):
    template_name = "profapp/grade/grade_list.djhtml"
    context_object_name = "grades"
    model = Grade
    sorter = Sorter("exam", "grade", "id", student="student__am", year="exam__subject__year", default="-grade")


    def get_context_data(self, **kwargs):
        stud = self.request.GET.get('stud')
	subj = self.request.GET.get('subj')
        exam = self.request.GET.get('exam')
        sort_by = self.request.GET.get('sort')

        if stud:
            kwargs['student'] = Student.objects.get(pk=stud)

	if subj:
            kwargs['subject'] = SemesterSubject.objects.get(pk=subj)

	if exam:
	    kwargs['exam'] = Exam.objects.get(pk=exam)

        return super(GradeListView, self).get_context_data(**kwargs)


    def get_queryset(self):
	filters = dict()
        stud = self.request.GET.get('stud')
	exam = self.request.GET.get('exam')
	subj = self.request.GET.get('subj')
        sort_by = self.request.GET.get('sort')

        if stud:
            filters['student'] = int(stud)
	if exam:
	    filters['exam'] = int(exam)
	if subj:
	    filters['exam__subject'] = int(subj)

	if filters:
	    ret = Grade.objects.filter(**filters)
	else:
            ret = super(GradeListView, self).get_queryset()

        return ret.order_by(self.sorter.order_col(sort_by))

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
