from cuentas.models import Cuentas
from equipo.models import Equipos,Equipo_Ec

def is_authenticate(user):
    return user.is_authenticated

def redirect_permision(user):
    if user.es_admin:
        return 'adminHome'
    elif user.is_ec:
        equipo_ec = Equipo_Ec.objects.get(ec=user)
        equipo = Equipos.objects.get(pk=equipo_ec.equipo_id)
        if equipo.is_active:
            return 'equipoHome'
        else:
            return 'home'
    else:
        return 'home'

def equipo_per(user):
    if is_authenticate(user):
        if user.is_ec:
            equipo_ec = Equipo_Ec.objects.get(ec=user)
            equipo = Equipos.objects.get(pk=equipo_ec.equipo_id)
            if equipo.is_active:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def admin_per(user):
    if is_authenticate(user):
        if user.es_admin:
            return True
        else:
            return False
    else:
        return False
