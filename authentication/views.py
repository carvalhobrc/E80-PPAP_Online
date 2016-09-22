from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from authentication.models import *
from django.http import HttpResponseRedirect, HttpResponse

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['inputName']
        password = request.POST['inputPassword']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            #Verify if user is Embraco's employee
            embraco_user = EmbracoProfile.objects.get(user=user.id)
            if embraco_user: #If is Embraco's user
                request.session['user_type'] = 'Embraco'
            else:
                supplier_user = SupplierProfile.objects.get(user=user.id)
                request.session['user_type'] = 'Supplier'
            if 'next' in request.GET:
                return HttpResponseRedirect(request.GET['next'])
            else:
                return HttpResponseRedirect('/')
        else:
            # Return an 'invalid login' error message
            return HttpResponseRedirect('/auth/login/')
    else:
        return render(request, 'authentication/login.html')

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/auth/login/')