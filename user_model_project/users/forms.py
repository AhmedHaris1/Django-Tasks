from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationFomr(UserCreationForm):

    model = CustomUser
    fields = ("email",) 
    
class CustomUserChangeForm(UserChangeForm):
    model = CustomUser
    fields = ("email",)
