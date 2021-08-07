from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from cuentas.forms import RegistroForm,Log_in_Form
from equipo.models import Equipo_Ec,Equipos
from cuentas.models import Cuentas
from django.contrib import messages
from cuentas import auth_fun



#Crear tu vistas aqui.


# Empiza funciones de ayuda
def is_authenticate(request):
    return request.user.is_authenticated

def redirect_permisions(user):
    if user.is_ec:
        equipo_ec = Equipo_Ec.objects.get(ec=user)
        equipo = Equipos.objects.get(pk=equipo_ec.equipo_id)
        if equipo.es_activo:
            return 'equipoHome'
        else:
            return 'home'
    elif user.es_admin:
        return 'adminHome'
    else:
        return 'home'

#fin de las funciones de ayuda

def registro_view(request):
    context={}
    if request.POST:
        form = RegistroForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context['form'] = form
    else:
        form = RegistroForm()
        context['form'] = form
    return render(request, 'cuentas/registro.html',context)


def login_view(request):
    context={}
    if auth_fun.is_authenticate(request.user):
            return redirect(auth_fun.redirect_permision(request.user))
    if request.POST:
        form = Log_in_Form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email,password=password)
            if user:
                login(request,user)
                return redirect(redirect_permisions(user))
            else:
                messages.add_message(request, messages.ERROR, 'Inicio de sesión no válido Inténtelo de nuevo')

    else:
        form = Log_in_Form()
    context['form'] = form
    return render(request, 'cuentas/login.html',context)


def logout_view(request):
    logout(request);
    # form = Log_in_Form()
    return redirect('login')
