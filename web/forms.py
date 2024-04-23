from django import forms
from .models import ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email','customer_name','message']
        labels = {
            'customer_email': 'Correo electrónico',
            'customer_name': 'Nombre',
            'message': 'Mensaje',
        }
    
    """ customer_email = forms.EmailField(label='correoeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
    customer_name  = forms.CharField(label='nombre')
    message = forms.CharField(label='mensaje',widget=forms.Textarea)
    
    """
    
    
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name',"last_name","email", "password1","password2"]