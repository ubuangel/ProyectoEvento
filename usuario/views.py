from django.shortcuts import render,redirect
from eventoapp.models import Eventos
from avisoConferencia.models import Avisos,Noticias
from cuentas.models import Cuentas
from cuentas.forms import RegistroForm
#from mainadmin.models import Academic_calendar
from equipo.models import Equipos,Equipo_Ec,Galeria
from equipo.forms import member_request_form
from django.views.decorators.clickjacking import xframe_options_sameorigin
# Cree sus vistas aquí


def galeria(request,nombreequipo):
    context = {}
    avisos = Avisos.objects.all().order_by('-creado_en')
    noticias = Noticias.objects.all().order_by('-creado_en')
    context['avisos'] = avisos
    context['noticias'] = noticias
    try:
        primeros_avisos = avisos[0]
    except:
        primeros_avisos = False
    try:
        primeras_noticias= noticias[0]
    except:
        primeras_noticias = False
    equipo = Equipos.objects.get(nombreequipo=nombreequipo)
    context['primeros_avisos']  = primeros_avisos
    context['primeras_noticias']  = primeras_noticias
    context['equipo'] = equipo
    context['images'] = Galeria.objects.all().filter(equipo=equipo).order_by('-fecha_subida')
    return render(request, 'galeria.html',context)

def equipo_ec_usuario(request,nombreequipo):
    context = {}
    avisos = Avisos.objects.all().order_by('-creado_en')
    noticias = Noticias.objects.all().order_by('-creado_en')
    context['avisos'] = avisos
    context['noticias'] = noticias
    try:
        primeros_avisos = avisos[0]
    except:
        primeros_avisos = False
    try:
        primeras_noticias= noticias[0]
    except:
        primeras_noticias = False
    equipo = Equipos.objects.get(nombreequipo=nombreequipo)
    cuentas = Equipo_Ec.objects.all().filter(equipo=equipo)
    context['primeros_avisos']  = primeros_avisos
    context['primeras_noticias']  = primeras_noticias
    context['equipo'] = equipo
    context['cuentas'] = cuentas
    return render(request, 'equipo_ec.html',context)

def todos_equipos_usuarios(request):
    context = {}
    avisos = Avisos.objects.all().order_by('-creado_en')
    noticias = Noticias.objects.all().order_by('-creado_en')
    context['avisos'] = avisos
    context['noticias'] = noticias
    try:
        primeros_avisos = avisos[0]
    except:
        primeros_avisos = False
    try:
        primeras_noticias= noticias[0]
    except:
        primeras_noticias = False
    context['equipos'] = Equipos.objects.all()
    context['primeros_avisos']  = primeros_avisos
    context['primeras_noticias']  = primeras_noticias
    return render(request, 'equipos.html',context)

def miembro_req(request,nombreequipo):
    context = {}
    avisos = Avisos.objects.all().order_by('-creado_en')
    noticias = Noticias.objects.all().order_by('-creado_en')
    context['avisos'] = avisos
    context['noticias'] = noticias
    try:
        primeros_avisos = avisos[0]
    except:
        primeros_avisos = False
    try:
        primeras_noticias= noticias[0]
    except:
        primeras_noticias = False
    context['primeros_avisos']  = primeros_avisos
    context['primeras_noticias']  = primeras_noticias
    equipo = Equipos.objects.get(nombreequipo=nombreequipo)
    context['equipo'] = equipo
    if request.POST:
        form = member_request_form(request.POST)
        if form.is_valid():
            miembro_req = form.save(commit=False)
            miembro_req.equipo = equipo
            miembro_req.save()
            context['form'] = member_request_form()
        else:
            context['form'] = form
    else:
        form = member_request_form()
        context['form'] = form
    return render(request, 'convertir_en_miembro_formulario.html',context)


def equipo_unico_usuario(request,nombreequipo):
    context = {}
    avisos = Avisos.objects.all().order_by('-creado_en')
    noticias = Noticias.objects.all().order_by('-creado_en')
    context['avisos'] = avisos
    context['noticias'] = noticias
    try:
        primeros_avisos = avisos[0]
    except:
        primeros_avisos = False
    try:
        primeras_noticias= noticias[0]
    except:
        primeras_noticias = False
    context['primeros_avisos']  = primeros_avisos
    context['primeras_noticias']  = primeras_noticias
    equipo = Equipos.objects.get(nombreequipo=nombreequipo)
    context['equipo'] = equipo
    eventos = Eventos.objects.all().filter(creado_por=equipo).order_by('-inicio_fecha')
    context['eventos'] = eventos
    return render(request, 'equipo_unico.html',context)



def calendario(request):
    context = {}
    avisos = Avisos.objects.all().order_by('-creado_en')
    noticias = Noticias.objects.all().order_by('-creado_en')
    context['avisos'] = avisos
    context['noticias'] = noticias
   # calendarios = Academic_calendar.objects.all().order_by('-uploaded_at')
    try:
        primeros_avisos = avisos[0]
    except:
        primeros_avisos = False
    try:
        primeras_noticias= noticias[0]
    except:
        primeras_noticias = False
    context['primeros_avisos']  = primeros_avisos
    context['primeras_noticias']  = primeras_noticias
   # context['calendarios'] = calendarios
    return render(request, 'academic.html',context)

@xframe_options_sameorigin
def calendario_label(request,label_name):
    context = {}
    avisos = Avisos.objects.all().order_by('-creado_en')
    noticias = Noticias.objects.all().order_by('-creado_en')
    context['avisos'] = avisos
    context['noticias'] = noticias
    try:
        primeros_avisos = avisos[0]
    except:
        primeros_avisos = False
    try:
        primeras_noticias= noticias[0]
    except:
        primeras_noticias = False
    context['primeros_avisos']  = primeros_avisos
    context['primeras_noticias']  = primeras_noticias
  #  context['caledar'] = Academic_calendar.objects.get(calendar_label=label_name)
    return render(request, 'calendario_unico.html',context)

def home(request):
    context = {}
    eventos = Eventos.objects.all().order_by('-inicio_fecha')
    avisos = Avisos.objects.all().order_by('-creado_en')
    noticias = Noticias.objects.all().order_by('-creado_en')
    context['avisos'] = avisos
    context['noticias'] = noticias
    try:
        primeros_avisos = avisos[0]
    except:
        primeros_avisos = False
    try:
        primeras_noticias= noticias[0]
    except:
        primeras_noticias = False
    context['primeros_avisos']  = primeros_avisos
    context['primeras_noticias']  = primeras_noticias

    if(len(eventos)>3):
        eventos = eventos[:3]
    context['eventos'] = eventos
    return render(request, 'index.html',context)

def evento_todos(request):
    context = {}
    context['eventos'] = Eventos.objects.all().order_by('-inicio_fecha')
    avisos = Avisos.objects.all().order_by('-creado_en')
    noticias = Noticias.objects.all().order_by('-creado_en')
    try:
        primeros_avisos = avisos[0]
    except:
        primeros_avisos = False
    try:
        primeras_noticias= noticias[0]
    except:
        primeras_noticias = False
    context['primeros_avisos']  = primeros_avisos
    context['primeras_noticias']  = primeras_noticias
    return render(request, 'eventos.html',context)

def perfil(request):
    context = {}
    avisos = Avisos.objects.all().order_by('-creado_en')
    noticias = Noticias.objects.all().order_by('-creado_en')
    try:
        primeros_avisos = avisos[0]
    except:
        primeros_avisos = False
    try:
        primeras_noticias= noticias[0]
    except:
        primeras_noticias = False
    context['primeros_avisos']  = primeros_avisos
    context['primeras_noticias']  = primeras_noticias
    if request.user.is_authenticated:
        context['user'] = request.user
        return render(request, 'perfil.html',context)
    else:
        return redirect('login')
def evento_unico(request,eventonombre):
    context = {}
    context['evento'] = Eventos.objects.get(eventonombre=eventonombre)
    eventos = Eventos.objects.all().order_by('-inicio_fecha')
    avisos = Avisos.objects.all().order_by('-creado_en')
    noticias = Noticias.objects.all().order_by('-creado_en')
    try:
        primeros_avisos = avisos[0]
    except:
        primeros_avisos = False
    try:
        primeras_noticias= noticias[0]
    except:
        primeras_noticias = False
    context['primeros_avisos']  = primeros_avisos
    context['primeras_noticias']  = primeras_noticias
    if(len(eventos)>3):
        eventos = eventos[:3]
    context['eventos'] = eventos
    return render(request, 'eventounico.html',context)


def unicoaviso(request,nombreavisos):
    context = {}
    context['avisos'] = Avisos.objects.get(avisotitulo=nombreavisos)
    avisos = Avisos.objects.all().order_by('-creado_en')
    noticias = Noticias.objects.all().order_by('-creado_en')
    try:
        primeros_avisos = avisos[0]
    except:
        primeros_avisos = False
    try:
        primeras_noticias= noticias[0]
    except:
        primeras_noticias = False
    context['primeros_avisos']  = primeros_avisos
    context['primeras_noticias']  = primeras_noticias
    context['all_news'] = avisos
    return render(request, 'avisosunicos.html',context)

def noticiain(request,noticename):
    context = {}
    context['notice'] = Noticias.objects.get(noticiatitulo=noticename)

    avisos = Avisos.objects.all().order_by('-creado_en')
    noticias = Noticias.objects.all().order_by('-creado_en')
    try:
        primeros_avisos = avisos[0]
    except:
        primeros_avisos = False
    try:
        primeras_noticias= noticias[0]
    except:
        primeras_noticias = False
    context['primeros_avisos']  = primeros_avisos
    context['primeras_noticias']  = primeras_noticias
    context['all_notice'] = noticias
    return render(request, 'noticiaunica.html',context)
