from django.shortcuts import render
from authentication.models import *
from .forms import *
from django.http import HttpResponseRedirect


def manageUsers(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        user_form = UserForm(request.POST)
        embraco_form = EmbracoUserForm(request.POST)
        # check whether it's valid:dj
        if user_form.is_valid() and embraco_form.is_valid():
            # process the data in form.cleaned_data as required
            created_user = user_form.save()
            embraco_form.cleaned_data['user'] = created_user.pk
            embraco_form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('manage-users/')

            # if a GET (or any other method) we'll create a blank form
    else:
        if request.session['user_type'] == 'Embraco':
            embraco_users = EmbracoProfile.objects.all()
        else:
            embraco_users = None
        supplier_users = SupplierProfile.objects.all()

        user_form = UserForm
        embraco_user_form = EmbracoUserForm

        return render(request,
                      'manageUsers/manage-users.html',
                      {
                          "embraco_users": embraco_users,
                          "supplier_users": supplier_users,
                          "user_form": user_form,
                          "embraco_user_form": embraco_user_form,
                      })
