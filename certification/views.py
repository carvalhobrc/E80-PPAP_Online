from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CertificationForm, DocumentsForm
from .models import Certification, RequiredCertificationDocuments, Documents

@login_required(login_url='/auth/login/')
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CertificationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            variable = form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/certification/new/' + str(variable.pk))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CertificationForm()
    return render(request, 'certification/certification-new.html', {"form": form})


@login_required(login_url='/auth/login/')
def editCertification(request, pk, template_name = 'certification/certification-new.html'):
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


def documentsView(request, pk):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        instance = Certification.objects.get(id=pk)
        # create a form instance and populate it with data from the request:
        formtest = DocumentsForm(request.POST)
        # check whether it's valid:
        if formtest.is_valid():
            # process the data in form.cleaned_data as required
            item_list = request.POST.getlist('documents_checkboxes[]', None)
            for item in item_list:
                doc_instance = Documents.objects.get(id=item)
                item_obj = RequiredCertificationDocuments(document_type=doc_instance, certification=instance)
                item_obj.save()
            return HttpResponseRedirect('/certification')
    # if a GET (or any other method) we'll create a blank form
    else:
        documents = Documents.objects.all()
    return render(request, 'certification/certification-new2.html', {"documents": documents})


def overview(request):
    return render(request, 'certification/overview.html')