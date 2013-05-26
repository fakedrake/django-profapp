from django.conf.urls import patterns, url
from django.conf import settings
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse


from profapp import views

urlpatterns = patterns('',
                       # url(r'^/$', RedirectView.as_view(url=reverse("student_list")), name="profapp_home"),
    url(r'^students/(?P<slug>\d+)/$', views.StudentDetailView.as_view(), name="student_view"),
    url(r'^students/$', views.StudentListView.as_view(), name="student_list"),
    url(r'^students/new/$', views.StudentCreateView.as_view(), name='student_create'),
    url(r'^students/(?P<slug>\d+)/update/$', views.StudentUpdateView.as_view(), name='update_student'),
    url(r'^students/(?P<slug>\d+)/delete/$', views.StudentDeleteView.as_view(), name='delete_student'),
                       #    url(r'^subjects/$', views.SemesterStudentListView.as_view()),
                       #    url(r'^submitsub/(?P<pk>\d+)/$', views.SemesterStudentCreateView.as_view()),
)
