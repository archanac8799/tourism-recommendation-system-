# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import PlacesForm
# Create your views here.
def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()

		return redirect("/home")
	else:
		form = RegisterForm()
	
	return render(response, "register/register.html", {"form":form})

def add_place(response):
	if response.method == "POST":
		form = PlacesForm(response.POST)
		if form.is_valid():
			form.save()

		return redirect("/home")
	else:
		form = PlacesForm()
	
	return render(response, "add_place.html", {"form":form})