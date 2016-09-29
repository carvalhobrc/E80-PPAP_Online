from django.shortcuts import render
from authentication.models import *
from .forms import *
from django.http import HttpResponseRedirect


def manageUsers(request):
    if request.session['user_type'] == 'Embraco':
        embraco_users = EmbracoProfile.objects.all()
    else:
        embraco_users = None
    supplier_users = SupplierProfile.objects.all()

    return render(request,
                  'manageUsers/manage-users.html',
                  {
                      "embraco_users": embraco_users,
                      "supplier_users": supplier_users,
                  })

def editEmbracoUser(request):
    instance = User.objects.get(id=2)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        user_form = UserForm(request.POST, instance=instance)
        embraco_form = EmbracoUserForm(request.POST, instance=instance.embracoprofile)
        # check whether it's valid:dj
        if user_form.is_valid() and embraco_form.is_valid():
            # process the data in form.cleaned_data as required
            created_user = user_form.save()
            created_embraco_user = embraco_form.save(commit=False)
            created_embraco_user.user = created_user
            created_embraco_user.save()
            # redirect to a new URL:
            return HttpResponseRedirect('manage-users/')
    else:
        user_form = UserForm
        embraco_user_form = EmbracoUserForm

        return render(request,
                      'manageUsers/embraco_user_edit.html',
                      {
                          "user_form": user_form,
                          "embraco_user_form": embraco_user_form,
                      })

def editSupplierUser(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        user_form = UserForm(request.POST)
        supplier_form = SupplierUserForm(request.POST)
        # check whether it's valid:dj
        if user_form.is_valid() and supplier_form.is_valid():
            # process the data in form.cleaned_data as required
            created_user = user_form.save()
            created_supplier_user = supplier_form.save(commit=False)
            created_supplier_user.user = created_user
            created_supplier_user.save()
            # redirect to a new URL:
            return HttpResponseRedirect('manage-users/')
    else:
        user_form = UserForm
        supplier_user_form = SupplierUserForm

        return render(request,
                      'manageUsers/manage-users.html',
                      {
                          "user_form": user_form,
                          "embraco_user_form": supplier_user_form,
                      })