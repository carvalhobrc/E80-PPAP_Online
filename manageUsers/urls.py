from django.conf.urls import url, include
from django.views.generic import DetailView
from authentication.models import *
from . import views

urlpatterns = [
    url(r'^$', views.manageUsers, name = 'manage-users'),
    url(r'^embraco/(?P<pk>\d+)$', DetailView.as_view(model=EmbracoProfile, template_name='manageUsers/embraco_user_detail.html')),
    url(r'^supplier/(?P<pk>\d+)$', DetailView.as_view(model=SupplierProfile, template_name='manageUsers/supplier_user_detail.html')),
]
