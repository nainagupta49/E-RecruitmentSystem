from django import forms
from .models import candidate

class RegisterForm(forms.ModelForm):
    class Meta:
        model = candidate
        fields = [
            'name',
            'email',
            'password',
            'birth_date',
            'gender',
            'phone'
        ]