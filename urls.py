from django.conf.urls import patterns, url

from profapp import views

urlpatterns = patterns('',
    url(r'^(?P<slug>\d+)/$', views.StudentDetailView.as_view()),
    url(r'^students/$', views.StudentListView.as_view()),
#    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
 #   url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
