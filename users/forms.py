from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
#from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm




class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
   
    
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password1', 'password2']
        
        
        
class UpdateForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = []
        
        
        

    