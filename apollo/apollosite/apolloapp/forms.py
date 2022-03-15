from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Ticket



class RegisterForm(UserCreationForm):
    email=forms.EmailField(max_length=100)

    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']


class TicketForm(forms.ModelForm):

    class Meta:
        model=Ticket
        fields=['title','description']

class SticketForm(forms.ModelForm):

    class Meta:
        model=Ticket
        fields='__all__'