from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect
from golfApp.models import Course, coursePar, Profile, Scorecard
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from golfApp.forms import createCourse, createScorecard, locate
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
import json

def home(request):
	return render(request, "golfApp/home.html")

#Courses Based on Location:

def locate(request):
	return

#Course Related:

def courseList(request):
	athlete_list = Course.objects.all()
	
def course(request, pk):
	course = get_object_or_404(Course, id=pk)
	return render(request, 'golfApp/course.html', {'course': course})

def formCourse(request):
	if request.POST:
		form = createCourse(request.POST)
		
		if form.is_valid():
			address = form.cleaned_data['address']
			latlon = Geocoder.geocode(address)
			form = form.save(commit=False)
			coords = Geocoder.geocode(address)
			coords = coords[0].coordinates
			lat = coords[0]
			lon = coords[1]
			latlon = str(lat)+","+str(lon)
			form.latlon = latlon
			form.save()
			return HttpResponseRedirect(reverse('home'))
	else:
		form = createCourse()
	args = {}
	args.update(csrf(request))

	args['form'] = form
	return render(request, 'golfApp/add_course.html', args)


#User/Profile Related:

def userLogin(request):
	c = {}
	c.update(csrf(request))
	return render_to_response(reverse('userLogin'), c)
	

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect(revers('userLoggedin'))
	else:
		return HttpResponseRedirect(reverse('invalid_login'))

def userLogout(request):
	return render_to_response("golfApp/user_logout.html")

def userSignUp(request):
	return render (request, "golfApp/userSignUp.html")

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/golfApp/register_success')
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	
	return render_to_response('golfApp/register.html', args)

def register_success(request):
	return render_to_response('golfApp/regester_success.html')

def profile(request, pk):
	profile = get_object_or_404(Profile, id=pk)
	return render(request, 'golfApp/profile.html', {'profile': profile})


#Static Content:

def games(request):
        return render (request, "golfApp/games.html")

def rules(request):
        return render (request, "golfApp/rules.html")

def userLogin(request):
	return render (request, "golfApp/user_login.html")
	

