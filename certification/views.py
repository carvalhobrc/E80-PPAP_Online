from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import CertificationForm

@login_required(login_url='/auth/login/')
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CertificationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('certification-list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CertificationForm()
    return render(request, 'certification/main.html', { "form": form })


#@login_required(login_url='/auth/login/')
#def editCertification(request, pk, template_name = 'certification/certification_edit.html'):
#    instance = User.objects.get(id=pk)
#    user_form = UserForm(request.POST or None, instance=instance)
#    embraco_user_form = EmbracoUserForm(request.POST or None, instance=instance.embracoprofile)
#    if request.method == 'POST':
#        # check whether it's valid:dj
#        if user_form.is_valid() and embraco_user_form.is_valid():
#            # process the data in form.cleaned_data as required
#            updated_user = user_form.save()
#            updated_embraco_user = embraco_user_form.save(commit=False)
#            updated_embraco_user.user = updated_user
#            updated_embraco_user.save()
#            # redirect to a new URL:
#            return HttpResponseRedirect('/manage-users/')
#    return render(request, template_name, { "user_form": user_form , "embraco_user_form": embraco_user_form,})


def overview(request):
    return render(request, 'certification/overview.html')