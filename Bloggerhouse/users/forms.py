from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class custom_user_creation_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repita su contraseña', widget = forms.PasswordInput)

    class Meta:
        model = User
        #campos que contendrá el formulario
        fields = ['username','email','password1','password2']
        help_texts = {k: '' for k in fields}
