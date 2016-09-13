from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['inputName']
        password = request.POST['inputPassword']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
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
