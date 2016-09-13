from django.conf.urls import url
from . import views
from django.views.generic import DetailView
from authentication.models import EmbracoProfile

urlpatterns = [
    url(r'^$',views.login, name='login'),
    url(r'^login/$',views.userLogin, name='login'),
    url(r'^logout/$',views.userLogout, name='logout'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=EmbracoProfile))
]