from django.shortcuts import render
from authentication.models import *
from .forms import *

def manageUsers(request):
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
