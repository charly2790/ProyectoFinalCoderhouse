from django import forms


class Users_form(forms.Form):
    email = forms.EmailField(max_length=40)
    password = forms.CharField(max_length=40)
    alias = forms.CharField(max_length=40)
    #rol = models.CharField(max_length=40,default = 'BLOGGER_BASIC')
    #fail_connection_attemps = models.IntegerField(default = 0)
    #blocked = models.BooleanField(default = True)
    #En lugar de datetime.now() django sugiere utilizar django.utils.timezone.now
    #dt_last_connection = models.DateTimeField(default = datetime.now())
    #dt_creation = models.DateTimeField(default = datetime.now())
    #bloggerhouse_level = models.CharField(max_length=40,default = 'BLOGGER_NEWBIE')