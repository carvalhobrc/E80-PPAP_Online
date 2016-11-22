from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PackagingRequirementsForm
from .models import PackagingRequirements, SupplierPackagingDescription, PackagingApproval

@login_required(login_url='/auth/login/')
def packagingRequirements(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PackagingRequirementsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            savedform = form.save()
            # redirect to a new URL:
            url = reverse('packaging_list', kwargs={'pk': savedform.pk})
            return HttpResponseRedirect(url)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PackagingRequirementsForm()
    return render(request, 'certification/certification-new.html', {"form": form})