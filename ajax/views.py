from django.shortcuts import render
from cuentas.models import Cuentas
from equipo.models import Equipos,Equipo_Ec,miembro
from eventoapp.models import Eventos,Detalles_par
from avisoConferencia.models import Avisos,Noticias
from django.http import JsonResponse
from django.template import Context, Template
from django.core.mail import send_mail
from django.conf import settings
from django.core import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from cuentas import auth_fun
# Create your views here.

def aprobar_miembro_request(request):
    data = {}

    if request.GET:
        equipoid = request.GET.get('equipoid')
        memid = int(request.GET.get('memid'))
        mem = miembro.objects.all().filter(pk=memid)[0]
        mem.aprobado = True
        mem.save()
        data['check'] = True
    return JsonResponse(data)

def eliminar_miembro_request(request):
    data = {}
    if request.GET:
        equipoid = request.GET.get('equipoid')
        memid = int(request.GET.get('memid'))
        mem = miembro.objects.all().filter(pk=memid)[0]
        mem.delete()
        data['check'] = True
    return JsonResponse(data)

def editar_evento(request):
    data = {}
    template = Template("equipo/eventounico.html")
    if request.GET:
        id = request.GET.get('id')
        evento_nombre = request.GET.get('evento_nombre')
        evento_lugar = request.GET.get('evento_lugar')
        evento_descripcion = request.GET.get('evento_descripcion')
        start_date_time = request.GET.get('start_date_time')
        end_date_time = request.GET.get('end_date_time')
        evento = Eventos.objects.get(pk = id)

        evento.eventonombre = evento_nombre
        evento.eventolugar = evento_lugar
        evento.descripcion = evento_descripcion
        evento.inicio_fecha = start_date_time
        evento.final_fecha = end_date_time
        try:
            evento.save()
            data['ok'] = True
        except Exception as e:
            data['ok'] = False
        context = Context({"evento": evento})
        template.render(context)
    return JsonResponse(data)

def actualizar_perfil(request):
    template = Template("perfil.html")
    data = {}
    if request.GET:
        email = request.GET.get('email')
        nombrecompleto = request.GET.get('nombrecompleto')
        celular = request.GET.get('celular')
        if request.user.email != email:
            try:
                user = Cuentas.objects.get(email=email)
            except Cuentas.DoesNotExist:
                user = None
        else:
            user = None
        if user:
            data['ok'] = False
            data['error'] = "Email ya existe"
        else:
            user = request.user
            user.nombrecompleto = nombrecompleto
            user.email = email
            user.numero_celular = celular
            data['ok'] = True
            user.save()
        return JsonResponse(data)

def cambiar_contraseña(request):
    data = {}
    if request.GET:
        old_password = request.GET.get('check_password')
        user = authenticate(email=request.user.email,password=old_password)
        if user:
            password = request.GET.get('password')
            confirm_password = request.GET.get('confirm_password')
            if password==confirm_password:
                try:
                    check = validate_password(password, user=None, password_validators=None)
                except ValidationError:
                    data['ok'] = False
                    check = ValidationError((password), code='invalid')
                if check == None:
                    user.password = make_password(password, salt=None, hasher='default')
                    user.save()
                    request.user = user
                    data['ok'] = True
                else:
                    data['error'] = "Puede ser que esta nueva contraseña sea demasiado semana"
            else:
                data['ok'] = False
                data['error'] = "La contraseña nueva y la contraseña de confirmación no coinciden"
        else:
            data['ok'] = False
            data['error'] = "La contraseña actual no coincide"
    return JsonResponse(data)

def eviaremail(request):
    data = {}
    if request.GET:
        if request.user.is_authenticated:
            if request.user.is_ec:
                equipo_ec = Equipo_Ec.objects.get(ec=request.user)
                equipo = Equipos.objects.get(pk=equipo_ec.equipo_id)
                id = request.GET.get('id')
                email_sub = request.GET.get('email_sub')
                participante = Detalles_par.objects.get(pk=id)
                email = participante.email
                email_msg = request.GET.get('email_msg')
                print("email MSg: " + email_msg)
                print("A : "+email)
                email_from = equipo.emailequipo
                email_pass = equipo.password
                recipient_list = [email,]
                # Formateo de mensajes
                email_msg = email_msg.replace("[[Nombre Participante]]",participante.nombre)
                email_msg = email_msg.replace("[[ID estudiante Participante]]",participante.std_id)
                email_msg = email_msg.replace("[[Participante Email]]",participante.email)
                email_msg = email_msg.replace("[[Participante celular]]",participante.celular)
                email_msg = email_msg.replace("[[Participante nombre]]",(participante.nombre.split())[0])
                # final Message Formatting

                send_mail( email_sub, email_msg, email_from, recipient_list,fail_silently=False, auth_user='dc9cfa69b22768', auth_password='b40b2aac7695c3')
        return JsonResponse(data)
#
# def shownews(request):
#     data = {}
#     # data['news'] = Avisos.objects.all()
#     data = serializers.serialize('json', Avisos.objects.all())
#     return JsonResponse(data)

def comprobar_datos_participante(request):
    data = {}
    if request.GET:
        email = request.GET.get('email')
        eventonombre = request.GET.get('eventonombre')

        evento  = Eventos.objects.get(eventonombre = eventonombre)
        data['ok'] = False
        check = Detalles_par.objects.filter(email=email).filter(evento=evento).count()
        if check>0:
            data['error'] = "Ya registre este evento"
        else:
            try:
                user = Detalles_par.objects.filter(email=email)[0]
            except Detalles_par.DoesNotExist:
                user = None
            if user:
                data['nombre'] = user.nombre
                data['std_id'] = user.std_id
                data['celular'] = user.celular
                data['ok'] = True

        return JsonResponse(data)


def registrar_participante(request):
    data = {}
    if request.GET:
        email = request.GET.get('email')
        nombre = request.GET.get('nombre')
        celular = request.GET.get('celular')
        std_id = request.GET.get('std_id')
        eventonombre = request.GET.get('eventonombre')
        evento  = Eventos.objects.get(eventonombre = eventonombre)
        equipo = Equipos.objects.get(nombreequipo = evento.creado_por)
        check = Detalles_par.objects.filter(email=email).filter(evento=evento).count()
        data['ok'] = False
        if check>0:
            data['error'] = "Esta registrado este evento"
        else:
            participantes_detalles = Detalles_par(nombre = nombre,std_id = std_id,email=email,celular=celular,evento=evento,equipo=equipo)
            participantes_detalles.save()
            data['ok'] = True
    return JsonResponse(data)


def agregar_ec_email_validar(request):
    data = {}
    email = request.GET['email']
    print(email)
    try:
        user = Cuentas.objects.get(email=email)
    except Cuentas.DoesNotExist:
        user = None
    #user = Cuentas.objects.get(email=email)
    data['check'] = False
    if user:
        if user.is_ec or user.es_admin:
            data['msg'] = "El usuario ya es un miembro  o un administrador"
        else:
            data['check'] = True
            data['email'] = user.email
            data['nombrecompleto'] = user.nombrecompleto
            data['numero_celular'] = user.numero_celular
    else:
        data['msg'] = "Usuario no encontrado"
    return JsonResponse(data)

def agregar_ec_datos_a_database(request):
    data = {}
    if request.GET:
        designacion = request.GET.get('designacion')
        nombreequipo = request.GET.get('nombreequipo')
        email = request.GET.get('email')

        equipo = Equipos.objects.get(nombreequipo=nombreequipo)
        ec =  Cuentas.objects.get(email = email)

        equipo_ec = Equipo_Ec(designacion = designacion,equipo = equipo,ec=ec)
        equipo_ec.save()
        ec.is_ec = True
        ec.save()
        all_ec = request.POST.getlist('ec')
        data['check'] = True
        data['msg'] = ec.nombrecompleto + "es un nuevo ec de " + nombreequipo

    return JsonResponse(data)

def desactivar_equipo(request):
    template = Template("admin/todosequipos.html")
    data = {}
    if request.GET:
        equipo = Equipos.objects.get(pk=request.GET.get('equipoid'))
        equipo.es_activo = False
        equipo.save()
        data['nombreequipo'] = equipo.nombreequipo
        data['check'] = True
        context = context = Context({"equipos": Equipos.objects.all()})
        template.render(context)
    return JsonResponse(data)


def activar_equipo(request):
    template = Template("admin/todosequipos.html")
    data = {}
    if request.GET:
        equipo = Equipos.objects.get(pk=request.GET.get('equipoid'))
        equipo.es_activo = True
        equipo.save()
        data['nombreequipo'] = equipo.nombreequipo
        data['check'] = True
        context = Context({"clubs": Equipos.objects.all()})
        template.render(context)
    return JsonResponse(data)

def eliminar_ec(request):
    template = Template("admin/todosequipos.html")
    data = {}
    if request.GET:
        equipo_ec = Equipo_Ec.objects.get(pk=request.GET.get('id'))
        ec_id  = equipo_ec.ec_id
        equipo_ec.delete()
        ec = Cuentas.objects.get(pk=ec_id)
        ec.is_ec = False
        ec.save()
        data['check'] = True
        # context = context = Context({"clubs": Equipos.objects.all()})
        # template.render(context)
    return JsonResponse(data)
