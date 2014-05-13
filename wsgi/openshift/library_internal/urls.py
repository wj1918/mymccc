from django.conf.urls import patterns, url

from library_internal import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^report/(?P<report_name>.+)$', views.report, name='report'),
)

