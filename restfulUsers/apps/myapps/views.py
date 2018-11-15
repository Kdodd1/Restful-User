from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import User

def index(request):
	context = {
	"users" : User.objects.all()
	}
	return render(request, "myapps/index.html", context)

def new(request):
	return render(request, "myapps/create.html")

def create(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):

		for key, value in errors.items():
			messages.error(request, value)

		return redirect('users/new')
	else:
		User.objects.create(first_name = request.POST['first_name'], email = request.POST['email'], last_name= request.POST['last_name'])
	return redirect('/users')

def show(request, number):
	context = {
	"user" : User.objects.get(id=(number))
	}
	return render(request, "myapps/show.html", context)

def edit(request, number):
	context = {
	"user" : User.objects.get(id=(number))
	}
	return render(request, "myapps/edit.html",context)

def update(request, number):
	errors = User.objects.basic_validator(request.POST)

	if len(errors):

		for key, value in errors.items():
			messages.error(request, value)

		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	else:
		user = User.objects.get(id=(number))
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()
	return redirect('/users')

def delete(request, number):
	user = User.objects.get(id=(number))
	user.delete()
	return redirect('/users')




