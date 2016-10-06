from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CertificationForm
from .models import Certification

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


@login_required(login_url='/auth/login/')
def editCertification(request, pk, template_name = 'certification/main.html'):
    instance = Certification.objects.get(id=pk)
    form = CertificationForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        # check whether it's valid:dj
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect("/certification/certification-list/" + str(instance.id))
    return render(request, template_name, { "form": form })


def overview(request):
    return render(request, 'certification/overview.html')