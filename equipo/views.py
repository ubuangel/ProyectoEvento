from django.shortcuts import render,redirect
from equipo.models import Equipo_Ec,Equipos,miembro
from eventoapp.models import Eventos,Detalles_par
from django.contrib import messages
from cuentas import auth_fun
from equipo.forms import actualizar_galeria
# Crear vistas aqui.

# Empiza funciones de ayuda
def is_authenticate(request):
    return request.user.is_authenticated

def redirect_permisions(user):
    if user.is_ec:
        return 'equipoHome'
    elif user.es_admin:
        return 'adminHome'
    else:
        return 'home'

#final de funciones de ayuda
def galeria(request):
    context={}
    if auth_fun.equipo_per(request.user):
        equipo_ec = Equipo_Ec.objects.get(ec=request.user)
        equipo = Equipos.objects.get(pk=equipo_ec.equipo_id)
        context['equipo'] = equipo
        if request.POST:
            form = actualizar_galeria(request.POST, request.FILES)
            if form.is_valid():
                gal = form.save(commit=False)
                gal.equipo = equipo
                gal.save()
                form = actualizar_galeria()
                context['form'] = form
                messages.add_message(request, messages.SUCCESS, 'Imagen cargada. Puede mostrarse en la vista de usuario')
            else:
                context['form'] = form
        else:
            form = actualizar_galeria()
            context['form'] = form

        return render(request, 'equipo/galeria.html',context)
    else:
        return redirect('login')
def miembros(request):
    context={}
    if auth_fun.equipo_per(request.user):
        equipo_ec = Equipo_Ec.objects.get(ec=request.user)
        equipo = Equipos.objects.get(pk=equipo_ec.equipo_id)
        miembros = miembro.objects.all().filter(equipo=equipo,aprobado=True)
        context['equipo'] = equipo
        context['miembros'] = miembros
        return render(request, 'equipo/todomiembros.html',context)
    else:
        return redirect('login')
def requests(request):
    context={}
    if auth_fun.equipo_per(request.user):
        equipo_ec = Equipo_Ec.objects.get(ec=request.user)
        equipo = Equipos.objects.get(pk=equipo_ec.equipo_id)
        mem_requests = miembro.objects.all().filter(equipo=equipo,aprobado=False)
        context['equipo'] = equipo
        context['miembros'] = mem_requests

        return render(request, 'equipo/requests.html',context)
    else:
        return redirect('login')

def equipoHome(request):
    context={}
    if auth_fun.equipo_per(request.user):
        equipo_ec = Equipo_Ec.objects.get(ec=request.user)
        equipo = Equipos.objects.get(pk=equipo_ec.equipo_id)
        hosted_num = Eventos.objects.filter(created_by = equipo).count()
        num_equipos = Equipos.objects.all().count()
        num_miembro = Detalles_par.objects.filter(equipo = equipo).count()
        tot_miembro = miembro.objects.all().filter(equipo = equipo).count()

        context['equipo'] = equipo
        context['num_hosted_event'] = hosted_num
        context['num_equipos'] = num_equipos
        context['num_miembro'] = num_miembro
        context['tot_miembro'] = tot_miembro
        return render(request, 'equipo/dashboard.html',context)
    else:
        return redirect('login')


def actualizar_email(request):
    context = {}
    if auth_fun.equipo_per(request.user):
        equipo_ec = Equipo_Ec.objects.get(ec=request.user)
        equipo = Equipos.objects.get(pk=equipo_ec.equipo_id)
        context['equipo'] = equipo
        if request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            equipo.emailequipo = email
            equipo.password = password
            equipo.save()
            messages.add_message(request, messages.SUCCESS, 'Email actualizado')
        return render(request, 'equipo/settings.html',context)
    else:
        return redirect('login')

def actualizar_description(request):
    context = {}
    if auth_fun.equipo_per(request.user):
        equipo_ec = Equipo_Ec.objects.get(ec=request.user)
        equipo = Equipos.objects.get(pk=equipo_ec.equipo_id)
        context['equipo'] = equipo
        if request.POST:
            descripcion = request.POST.get('descripcion')
            equipo.descripcion = descripcion
            equipo.save()
            messages.add_message(request, messages.SUCCESS, 'Descripcion del equipo actualizado')
        return render(request, 'equipo/settings.html',context)
    else:
        return redirect('login')

def settings(request):
    context = {}
    if auth_fun.equipo_per(request.user):
        equipo_ec = Equipo_Ec.objects.get(ec=request.user)
        equipo = Equipos.objects.get(pk=equipo_ec.equipo_id)
        context['equipo'] = equipo
        if request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            equipo.emailequipo = email
            equipo.password = password
            equipo.save()
            messages.add_message(request, messages.SUCCESS, 'Email Actualizado')
        return render(request, 'equipo/settings.html',context)
    else:
        return redirect('login')
