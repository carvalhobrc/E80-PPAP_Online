from django.conf.urls import url
from . import views
from .models import PackagingRequirements

urlpatterns = [
    #url(r'^$', ListView.as_view(queryset=PackagingRequirements.objects.all().order_by("-id"),template_name="certification/certification-list.html"), name='packaging_list'),
    url(r'^$', views.packagingRequirements, name = 'packaging_requirements_new'),
]
