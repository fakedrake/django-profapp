from django.conf.urls import patterns, url
from django.conf import settings
from django.core.urlresolvers import reverse

from profapp.views import student


urlpatterns = patterns('',
    url(r'^students/(?P<slug>\d+)/$', student.StudentDetailView.as_view(), name="student_view"),
    url(r'^students/$', student.StudentListView.as_view(), name="student_list"),
    url(r'^students/new/$', student.StudentCreateView.as_view(), name='student_create'),
    url(r'^students/(?P<slug>\d+)/update/$', student.StudentUpdateView.as_view(), name='update_student'),
    url(r'^students/(?P<slug>\d+)/delete/$', student.StudentDeleteView.as_view(), name='delete_student'),
    url(r'^home/$', student.StudentListView.as_view(), name="profapp_home"),

                       #    url(r'^subjects/$', views.SemesterStudentListView.as_view()),
                       #    url(r'^submitsub/(?P<pk>\d+)/$', views.SemesterStudentCreateView.as_view()),
)
