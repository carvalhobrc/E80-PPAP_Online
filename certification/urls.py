from django.conf.urls import url, include
from django.views.generic import DetailView, ListView
from certification.models import Certification
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'certification'),
    url(r'^overview/$', views.overview, name = 'overview'),
    url(r'^certification-list/$', ListView.as_view(queryset=Certification.objects.all().order_by("id")[:25], template_name="certification/certification-list.html")),
    url(r'^certification-list/(?P<pk>\d+)/$', DetailView.as_view(model=Certification, template_name='certification/certification.html')),
    url(r'^certification-list/(?P<pk>\d+)/edit$', views.editCertification, name='certification-edit'),
]
