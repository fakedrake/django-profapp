from django.conf.urls import patterns, url
from django.conf import settings
from django.core.urlresolvers import reverse

from profapp.views import student, semestersubject


urlpatterns = patterns('',
    url(r'^students/(?P<slug>\d+)/$', student.StudentDetailView.as_view(), name="student_view"),
    url(r'^students/$', student.StudentListView.as_view(), name="student_list"),
    url(r'^students/new/$', student.StudentCreateView.as_view(), name='student_create'),
    url(r'^students/(?P<slug>\d+)/update/$', student.StudentUpdateView.as_view(), name='update_student'),
    url(r'^students/(?P<slug>\d+)/delete/$', student.StudentDeleteView.as_view(), name='delete_student'),
    url(r'^home/$', student.StudentListView.as_view(), name="profapp_home"),

#    url(r'^subjects/(?P<slug>\d+)/$', semestersubject.SubjectDetailView.as_view(), name="subject_view"),
#    url(r'^subjects/$', semestersubject.SubjectListView.as_view(), name="subject_list"),
                       #    url(r'^submitsub/(?P<pk>\d+)/$', views.SemesterStudentCreateView.as_view()),
    url(r'^subjects/(?P<slug>[\w-]+)/(?P<year>\d+)/$', semestersubject.SubjectYearDetailView.as_view(), name="subject_year_view"),
    url(r'^subjects/(?P<slug>[\w-]+)/$', semestersubject.SubjectYearListView.as_view(), name="subject_year_list"),


)
