from django import forms
from equipo.models import Equipos,miembro,Galeria

class registroEquipo(forms.ModelForm):
    """docstring for ."""
    nombreequipo = forms.CharField(max_length = 60, widget = forms.TextInput(attrs={'class':'form-control','placeholder':"Nombre del equipo"}))
    nombre_corto = forms.CharField(max_length = 60, widget = forms.TextInput(attrs={'class':'form-control','placeholder':"nombre corto del equipo aqui"}))
    logo = forms.ImageField(widget = forms.FileInput(attrs={'class':'form-control','placeholder':"Logo aqui"}))
    # nombre_corto = forms.TextInput(attrs={'class':'form-control','placeholder':"Equipo Name Here"})
    # nombre_corto = forms.FileInput(attrs={'class':'form-control','placeholder':"Equipo Name Here"})

    class Meta:
        """docstring for ."""
        model = Equipos
        fields = ('nombreequipo','nombre_corto','logo')

class actualizar_galeria(forms.ModelForm):
    """docstring for ."""
    imagen = forms.ImageField(label="Galeria Imagen",widget = forms.FileInput(attrs={'class':'form-control','placeholder':"Imagen Galeria"}))
    # nombre_corto = forms.TextInput(attrs={'class':'form-control','placeholder':"Equipo Name Here"})
    # nombre_corto = forms.FileInput(attrs={'class':'form-control','placeholder':"     Equipo Name Here"})

    class Meta:
        """docstring for ."""
        model = Galeria
        fields = ('imagen',)

class member_request_form(forms.ModelForm):
    """docstring for ."""
    nombre = forms.CharField(label="Nombre completo",widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese su nombre completo'}))
    email = forms.EmailField(label="Email Address",help_text="Nunca compartiremos su correo electrónico con nadie más.", widget= forms.EmailInput(attrs={'class': 'form-control','aria-describedby':'emailHelp','placeholder':'Enter email'}))
    std_id = forms.CharField(label=" ID estudiante",widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Id de estudiante'}))
    numero_celular = forms.CharField(label="Numero de celular",widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese su numero de telefono'}))
    semestre = forms.IntegerField(label="Number Of Semister",max_value=21,min_value=0,widget= forms.NumberInput(attrs={'class': 'form-control','placeholder':'Ingrese su semestre'}))
    credito_completado = forms.IntegerField(label="Completo creditos",min_value=0,widget= forms.NumberInput(attrs={'class': 'form-control','placeholder':'Ingrese sus creditos completos'}))


    class Meta:
        """docstring for ."""
        model = miembro
        fields = ('nombre','std_id','email','numero_celular','semestre','credito_completado')
