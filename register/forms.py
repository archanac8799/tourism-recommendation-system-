from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Place

class RegisterForm(UserCreationForm):
		email = forms.EmailField()

		class Meta:
			model = User
			fields = ["email","username",  "password1", "password2"]

class PlacesForm(forms.ModelForm):
		place = forms.CharField()

		class Meta:
			model = Place
			fields = ["place","country"]

