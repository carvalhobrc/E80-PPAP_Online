from django.shortcuts import render

def manageUsers(request):
    return render(request, 'manageUsers/manage-users.html')
