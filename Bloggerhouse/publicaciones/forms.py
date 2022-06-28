from django import forms
from publicaciones.models import publicacion

class Publicacion_form(forms.ModelForm):
    class Meta:
        model = publicacion
        #fields = '__all__'
        fields = ['title','category','main_image','content']