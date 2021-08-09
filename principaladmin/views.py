from django.shortcuts import render,redirect
from equipo.forms import registroEquipo
from principaladmin.forms import upload_calendar_form
from cuentas.models import Cuentas
from equipo.models import Equipos,Equipo_Ec
from cuentas import auth_fun

# Create your views here.
def mainAdmin(request):
    if auth_fun.admin_per(request.user):
        return render(request, 'admin/admin.html')
    else:
        return redirect('login')


def uploadcalendar(request):
    context={}
    if auth_fun.admin_per(request.user):
        if request.POST:
            form = upload_calendar_form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('adminHome')
            else:
                context['form'] = form
        else:
            form = upload_calendar_form()
            context['form'] = form
        return render(request, 'admin/agregarcalendario.html',context)
    else:
        return redirect('login')



def registerclub(request):
    context={}
    if auth_fun.admin_per(request.user):
        if request.POST:
            form = registroEquipo(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('adminHome')
            else:
                context['form'] = form
        else:
            form = registroEquipo()
            context['form'] = form
        return render(request, 'admin/crearequipo.html',context)
    else:
        return redirect('login')

def allclubs(request):
    if auth_fun.admin_per(request.user):
        context={}
        context['equipos'] = Equipos.objects.all()
        return render(request, 'admin/todosequipos.html',context)
    else:
        return redirect('login')


def clubsingle(request,clubname):
    context={}
    if auth_fun.admin_per(request.user):
        equipo = Equipos.objects.get(clubname=clubname)
        club_ec = Equipo_Ec.objects.filter(equipo=equipo).values('id','ec_id__username','ec_id__email','ec_id__phone_number','date_joined','club__clubname','designation')
        context['details'] = club_ec
        context['equipo'] = equipo
        if request.POST:
            print("hello")
        return render(request, 'admin/equipounico.html',context)
    else:
        return redirect('login')
