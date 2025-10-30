from django.shortcuts import render
from Menu_Dinamico.models import Trabajador, Rol, Usuarios, Historial_Login, Sucursal, Permisos, Surcursal_Permisos, Menu
# Create your views here.
def iniciomenuDef(request):
    menu = Menu.objects.values()
    return render(request, 'index.html', {"list": menu})
def pruebaDef(request):
    return render(request,'inicio.html',{})