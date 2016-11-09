from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login/')
def index(request):
    return render(request, 'main/side-menu.html', {'menuItems':['FMEA de Process', 'Alvará', 'Mapa de Processo']})