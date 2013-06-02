import datetime
import mimetypes
from StringIO import StringIO

from django import forms
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.extras.widgets import SelectDateWidget
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from profapp.models import Exam, Grade, SemesterSubject
from profapp.forms import ExamForm


class ExamListView(ListView):
    template_name = "profapp/exam/exam_list.djhtml"
    context_object_name = "exams"
    model = Exam

    def get_context_data(self, **kwargs):
        subj = self.request.GET.get('subj')
        if subj:
            kwargs['subject'] = SemesterSubject.objects.get(pk=int(subj))

        return super(ExamListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        subj = self.request.GET.get('subj')
        if subj:
            return Exam.objects.filter(subject=int(subj))
        else:
            return super(ExamListView, self).get_queryset()


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

class ExamDetailView(DetailView):
    template_name = "profapp/exam/exam_details.djhtml"
    context_object_name = "exam"
    model = Exam

    def get_context_data(self, **kwargs):
        kwargs['grade_count'] = len(Grade.objects.filter(exam=self.object.pk))
 
	return super(ExamDetailView, self).get_context_data(**kwargs)
  
    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('download'):
            fd = self.object.question_set.file
            stream = StringIO(fd.read())
            mimetype = mimetypes.guess_type(self.object.question_set.url)
            return HttpResponse(stream.read(), mimetype=mimetype)
        else:
            return super(ExamDetailView, self).render_to_response(context, **response_kwargs)
