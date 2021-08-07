from django import forms
from django.contrib.auth.forms import UserCreationForm
from cuentas.models import Cuentas
from django.contrib.auth import authenticate

class RegistroForm(UserCreationForm):
    """docstring for ."""
    image = forms.ImageField(label="Sube tu imagen",widget = forms.FileInput(attrs={'class':'form-control','placeholder':"Su imagen"}))
    nombrecompleto = forms.CharField(label="Full Name",widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese nombre completo'}))
    email = forms.EmailField(label="Direccion Email ",help_text="Nunca compartiremos su correo electrónico con nadie más.", widget= forms.EmailInput(attrs={'class': 'form-control','aria-describedby':'emailHelp','placeholder':'Enter email'}))
    nombreusuario = forms.CharField(label="NombreUsuario",widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese nombreusuario'}))
    numero_celular = forms.CharField(label=" Numero de telefono",widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese numero de celular'}))
    password1 = forms.CharField(label="Password",help_text="No comparta su contraseña con otras personas ",widget= forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter Password'}))
    password2 = forms.CharField(label="Confirmar Password",help_text="",widget= forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Re-Enter Password'}))


    class Meta:
        """docstring for ."""
        model = Cuentas
        fields = ('image','nombrecompleto','email','nombreusuario','numero_celular','password1','password2')


class Log_in_Form(forms.Form):
    """docstring for ."""
    email = forms.EmailField(label=" Direccion Email",help_text="Nunca compartiremos su correo electrónico con nadie más..", widget= forms.EmailInput(attrs={'class': 'form-control','aria-describedby':'emailHelp','placeholder':'Enter email'}))
    password = forms.CharField(label="Password",help_text="No comparta su contraseña con otras personas.",widget= forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter Password'}))
    class Meta:
        """docstring for ."""
        model = Cuentas
        fields = ('email','password')

        def clean(self):
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email,password=password):
                raise forms.ValidationError(" login invalido")
