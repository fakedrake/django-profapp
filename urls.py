from django.conf.urls import patterns, url
from django.conf import settings
from django.core.urlresolvers import reverse

from profapp.views import student, semestersubject, exam, grade


urlpatterns = patterns('',
    url(r'^students/(?P<slug>\d+)/$', student.StudentDetailView.as_view(), name="student_view"),
    url(r'^students/$', student.StudentListView.as_view(), name="student_list"),
    url(r'^students/new/$', student.StudentCreateView.as_view(), name='student_create'),
    url(r'^students/(?P<slug>\d+)/update/$', student.StudentUpdateView.as_view(), name='update_student'),
    url(r'^students/(?P<slug>\d+)/delete/$', student.StudentDeleteView.as_view(), name='delete_student'),

    url(r'^subjects/new/$', semestersubject.SemesterSubjectCreateView.as_view(), name='subject_create'),
    url(r'^subjects/(?P<pk>\d+)/$', semestersubject.SubjectYearDetailView.as_view(), name="subject_year_view"),
                       url(r'^subjects/(?P<slug>[\w ]+)/$', semestersubject.SubjectYearListView.as_view(), name="subject_year_list"),
    url(r'^subjects/(?P<pk>\d+)/update/$', semestersubject.SemesterSubjectUpdateView.as_view(), name='update_subject'),
    url(r'^subjects/(?P<pk>\d+)/delete/$', semestersubject.SemesterSubjectDeleteView.as_view(), name='delete_subject'),
    url(r'^subjects/$', semestersubject.SubjectListView.as_view(), name="subject_list"),

    url(r'^exams/new/$', exam.ExamCreateView.as_view(), name="exam_create"),
    url(r'^exams/$', exam.ExamListView.as_view(), name="exam_view"),
    url(r'^exams/(?P<pk>\d+)/$', exam.ExamDetailView.as_view(), name="exam_details"),
    url(r'^exams/(?P<pk>\d+)/delete/$', exam.ExamDeleteView.as_view(), name="delete_exam"),
    url(r'^exams/(?P<pk>\d+)/update/$', exam.ExamUpdateView.as_view(), name="update_exam"),

    url(r'^grade/new/$', grade.GradeCreateView.as_view(), name="grade_create"),
    url(r'^grades/$', grade.GradeListView.as_view(), name="grade_list"),
    url(r'^grades/(?P<pk>\d+)/update/$', grade.GradeUpdateView.as_view(), name="update_grade"),
    url(r'^grades/(?P<pk>\d+)/delete/$', grade.GradeDeleteView.as_view(), name="delete_grade"),

    url(r'^home/$', student.StudentListView.as_view(), name="profapp_home"),
)
