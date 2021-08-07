from django import forms
from avisoConferencia.models import Avisos,Noticias

class agregaravisosform(forms.ModelForm):
    """docstring for ."""
    avisotitulo = forms.CharField(max_length = 255, widget = forms.TextInput(attrs={'class':'form-control','placeholder':"Título  aquí"}))
    descripcion = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control','placeholder':"Aviso aqui"}))

    class Meta:
        """docstring for ."""
        model = Avisos
        fields = ('avisotitulo','descripcion')

class agregarnoticiasform(forms.ModelForm):
    """docstring for ."""
    noticiatitulo = forms.CharField(max_length = 255, widget = forms.TextInput(attrs={'class':'form-control','placeholder':"Titulo de noticia aqui"}))
    descripcion = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control','placeholder':"Noticia Aqui"}))

    class Meta:
        """docstring for ."""
        model = Noticias
        fields = ('noticiatitulo','descripcion')
