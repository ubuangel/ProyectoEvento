from django.shortcuts import render,redirect
from avisoConferencia.forms import agregaravisosform,agregarnoticiasform
from avisoConferencia.models import Avisos,Noticias
from django.http import HttpResponse
from cuentas import auth_fun
# crear vistas aqui
def agregaravisos(request):
    context={}
    context['success_msg'] = ""
    if auth_fun.admin_per(request.user):
        if request.POST:
            form = agregaravisosform(request.POST)
            if form.is_valid():
                form.save()
                form = agregaravisosform()
                context['form'] = form
                context['success_msg'] = "Esta agregado. Esto se mostrará al usuario "
            else:
                context['form'] = form
        else:
            form = agregaravisosform()
            context['form'] = form
        return render(request, 'admin/agregaraviso.html',context)
    else:
        return redirect('login')


def agregarnoticias(request):
    context={}
    context['success_msg'] = ""
    if auth_fun.admin_per(request.user):
        if request.POST:
            form = agregarnoticiasform(request.POST)
            if form.is_valid():
                form.save()
                form = agregarnoticiasform()
                context['form'] = form
                context['success_msg'] = "Esta agregado. Esto se mostrará al usuario "
            else:
                context['form'] = form
        else:
            form = agregarnoticiasform()
            context['form'] = form
        return render(request, 'admin/agregarnoticias.html',context)
    else:
        return redirect('login')


def todoavisos(request):
    context = {}
    if auth_fun.admin_per(request.user):
        context['news_all'] = Avisos.objects.all()
        return render(request, 'admin/todosavisos.html',context)
    else:
        return redirect('login')



def eliminaraviso(request,id):
    context = {}
    if auth_fun.admin_per(request.user):
        try:
            avisos = Avisos.objects.get(pk=id)
        except Avisos.DoesNotExist:
            avisos = None
        if avisos:
            avisos.delete()
            return redirect('todoavisos')
        else:
            return HttpResponse("No exit")
    else:
        return redirect('login')


def todonoticias(request):
    context = {}
    if auth_fun.admin_per(request.user):
        context['noticias'] = Noticias.objects.all()
        return render(request, 'admin/todasnoticias.html',context)
    else:
        return redirect('login')



def eliminarnoticia(request,id):
    context = {}
    if auth_fun.admin_per(request.user):
        try:
            noticia = Noticias.objects.get(pk=id)
        except Noticias.DoesNotExist:
            noticia = None

        if noticia:
            noticia.delete()
            return redirect('todonoticias')
        else:
            return HttpResponse(" No Exit")
    else:
        return redirect('login')
