from django import forms
from principaladmin.models import clendario_Academico

class upload_calendar_form(forms.ModelForm):
    """docstring for ."""
    calendario_label = forms.CharField(max_length = 60, widget = forms.TextInput(attrs={'class':'form-control','placeholder':"Label Of this file"}))
    file = forms.FileField(widget = forms.FileInput(attrs={'class':'form-control','placeholder':"Pdf file of academic_ calendar"}))

    class Meta:
        """docstring for ."""
        model = clendario_Academico
        fields = ('calendario_label','file')
