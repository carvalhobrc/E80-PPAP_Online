from django.conf.urls import url
from django.views.generic import DetailView
from authentication.models import *
from . import views

urlpatterns = [
    url(r'^$', views.manageUsers, name = 'manage-users'),
    url(r'^embraco/new/$', views.editEmbracoUser, name = 'new-user'),
    url(r'^supplier/new/$', views.editSupplierUser, name = 'new-supplier'),
    url(r'^embraco/(?P<pk>\d+)$', views.editEmbracoUser, name = 'edit-user-info'),
    url(r'^supplier/(?P<pk>\d+)$', views.editSupplierUser, name = 'edit-supplier-info'),
]
