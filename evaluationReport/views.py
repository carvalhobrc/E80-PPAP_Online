from django.shortcuts import render
from django.urls import reverse
from certification.functions import verify_certification_session
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
@login_required(login_url='/auth/login/')
def characteristics(request, template_name = 'evaluationReport/characteristics.html'):
    sel_certification = verify_certification_session(request)
    if not sel_certification:
        url = reverse('certification-list')
        return HttpResponseRedirect(url)
    #
    # instance = EmbracoProfile.objects.get(id=pk)
    # user_form = UserForm(request.POST or None, instance=instance.user)
    # embraco_user_form = EmbracoUserForm(request.POST or None, instance=instance)
    # if request.method == 'POST':
    #     # check whether it's valid:dj
    #     if user_form.is_valid() and embraco_user_form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         updated_user = user_form.save()
    #         updated_embraco_user = embraco_user_form.save(commit=False)
    #         updated_embraco_user.user = updated_user
    #         updated_embraco_user.save()
    #         # redirect to a new URL:
    #         url = reverse('characteristics', kwargs={'action': 'list_embraco_users'})
    #         return HttpResponseRedirect(url)
    # return render(request, template_name, { "characteristics": characteristics_list , "embraco_user_form": embraco_user_form,})
    return