from django.shortcuts import render,redirect
from equipo.models import Equipos,Equipo_Ec
from eventoapp.models import Eventos,Detalles_par
from django.contrib import messages
from cuentas import auth_fun

# Crear vistas aqui.
#------------------- Funciones auxiliares --------------------

def ec_es_autenticar(request):
    temp = {}
    if auth_fun.equipo_per(request.user):
        temp['auth'] = True
        equipo_ec = Equipo_Ec.objects.get(ec=request.user)
        equipo = Equipos.objects.get(pk=equipo_ec.equipo_id)
        temp['equipo'] = equipo
    else:
        temp['auth'] = False
    print(temp)
    return temp

def crear_evento_db(request):
    temp =  {}
    event_cover_photo = request.FILES.get('evet_cover')
    eventonombre= request.POST.get('evento_nombre')
    eventolugar = request.POST.get('evento_lugar')
    descripcion = request.POST.get('evento_descripcion')
    inicio_fecha = request.POST.get('start_date_time')
    final_fecha = request.POST.get('end_date_time')
    equipo_ec = Equipo_Ec.objects.get(ec=request.user)
    equipo = Equipos.objects.get(pk=equipo_ec.equipo_id)
    print(event_cover_photo)
    evento =  Eventos(event_cover_photo=event_cover_photo,eventonombre=eventonombre,eventolugar=eventolugar,description=description,inicio_fecha=inicio_fecha,enddate=enddate,creado_por = equipo)
    try:
        evento.save()
        temp['check'] = True
        temp['evento'] = evento
    except Exception as e:
        # print(e, e.__class__)
        temp['check'] = False
    return temp




#-------------------final ayuda ------------------------------

def crearevento(request):
    context = {}
    temp = ec_es_autenticar(request)
    if temp['auth']:
        context['equipo'] = temp['equipo']
        if request.POST:
            temp = crear_evento_db(request)
            if temp['check']:
                messages.add_message(request, messages.SUCCESS, 'Evento creado correctamente')
            else:
                messages.add_message(request, messages.ERROR, 'Se produjo un error. Inténtelo de nuevo. Posible entrada duplicada')

        return render(request, 'equipo/creareventos.html',context)
        #return render(request, 'templates/eventos/createevents.html',context)
    else:
        return redirect('login')


def organizados_eventos(request):
    context = {}
    temp = ec_es_autenticar(request)
    if temp['auth']:
        context['equipo'] = temp['equipo']
        equipo = temp['equipo']
        context['eventos'] = Eventos.objects.filter(creado_por = equipo)
        return render(request, 'equipo/hosted.html',context)
    else:
        return redirect('login')

def eventosunicos(request,eventonombre):
    context = {}
    temp = ec_es_autenticar(request)
    if temp['auth']:
        context['equipo'] = temp['equipo']
        equipo = temp['equipo']
        context['evento'] = Eventos.objects.filter(eventonombre=eventonombre)[0];
        return render(request, 'equipo/eventounico.html',context)
    else:
        return redirect('login')


def participantes(request):
    context = {}
    temp = ec_es_autenticar(request)
    if temp['auth']:
        context['equipo'] = temp['equipo']
        equipo = temp['equipo']
        context['eventos'] = Eventos.objects.filter(creado_por = equipo).order_by('-inicio_fecha')
        return render(request, 'equipo/participantes.html',context)
    else:
        return redirect('login')


def Detalles_par(request,eventonombre):
    context = {}
    temp = ec_es_autenticar(request)
    if temp['auth']:
        context['equipo'] = temp['equipo']
        equipo = temp['equipo']
        check = Eventos.objects.filter(eventonombre=eventonombre).filter(creado_por=equipo).count()
        if check==0:
            return redirect('participantes')
        else:
            evento = Eventos.objects.filter(eventonombre=eventonombre)[0]
            context['participantes'] = Detalles_par.objects.filter(evento = evento)
            return render(request, 'equipo/detallesdeparticipante.html',context)
    else:
        return redirect('login')
