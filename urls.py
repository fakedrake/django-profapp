from django.conf.urls import patterns, url

from profapp import views

urlpatterns = patterns('',
    url(r'^(?P<slug>\d+)/$', views.StudentDetailView.as_view()),
    url(r'^students/$', views.StudentListView.as_view()),
    url(r'^submit_student/$', views.StudentCreateView.as_view()),
    url(r'^students/update/(?P<slug>\d+)/$', views.StudentUpdateView.as_view()),
#    url(r'^subjects/$', views.SemesterStudentListView.as_view()),
#    url(r'^submitsub/(?P<pk>\d+)/$', views.SemesterStudentCreateView.as_view()),
)
