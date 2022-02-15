from django import forms
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

name_validator = RegexValidator(r'^[a-zA-Z]*$', "Only alphabets are allowed.")

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
        'placeholder':'Enter a username', 'type':'text'}), error_messages={'unique':'Username already taken.'})
    
    first_name = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={
        'placeholder':'Your first name', 'type':'text'}), validators=[name_validator])
    
    last_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
        'placeholder':'your last name', 'type':'text'}), validators=[name_validator])
    
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'placeholder':'your email address', 'type':'email'}),)

    
    
    password = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
        'placeholder':'Enter Password', 'type':'password'}),)
    
    password2 = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
        'placeholder':'Confirm Password', 'type':'password'}),)

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):
        super().clean()
        cd = self.cleaned_data
        password = cd.get('password')
        password2 = cd.get('password2')
        if password != password2:
            raise ValidationError("Please enter same password.")
