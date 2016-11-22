from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Certification.objects.all().order_by("-id"),template_name="certification/certification-list.html"), name='packaging_list'),
    url(r'^new$', views.index, name = 'packaging_requirements_new'),
]
