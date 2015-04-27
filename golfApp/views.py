from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect
from golfApp.models import Course, coursePar, Profile, Scorecard
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from golfApp.forms import createCourse, createScorecard, locate
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.serializers.json import Serializer

from datetime import datetime
import json
from geopy import GoogleV3

serializer = Serializer()

def filter(request):
	f = courseFilter(request.GET, queryset=Course.objects.all())
	return render_to_response('golfApp/map.html',{'filter': f})


def home(request):
	print request.user
	return render(request, 'golfApp/home.html')

def locate(request):
	courses = Course.objects.all()
	context = {
		'courses' : courses
	}
	return render (request, "golfApp/map.html", context)

#Courses Based on Location:


#Course Related:

def courseList(request):
	course_list = Course.objects.all()
	courses_json = serializer.serialize(course_list)
	return render(request, 'golfApp/course-list.html', {
		'courses': course_list,
		'courses_json': courses_json,
	})
	
def course(request, pk):
	course = get_object_or_404(Course, id=pk)
	return render(request, 'golfApp/course-profile.html', {'course': course})

def formCourse(request):
	if request.POST:
		form = createCourse(request.POST)
		
		if form.is_valid():
			address = form.cleaned_data['address']
			form = form.save(commit=False)
			google = GoogleV3()
			coords = google.geocode(address)
			lat = coords.latitude
			lon = coords.longitude
			latlon = str(lat)+","+str(lon)
			form.latlon = latlon
			form.save()
			return HttpResponseRedirect(reverse('home'))
	else:
		form = createCourse()
	args = {}
	args.update(csrf(request))

	args['form'] = form
	return render(request, 'golfApp/add-course.html', args)


#User/Profile Related:

def userLogin(request):
	
	failedlogin = False
	if request.method =='POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = auth.authenticate(username=username, password=password)
	
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect(reverse('home'))
		else:
			failedlogin = True
			
		
	return render (request, "golfApp/user-login.html", {"failedlogin":failedlogin})

def userLogout(request):
	
	auth.logout(request)
	
	return HttpResponseRedirect(reverse('home'))

def userSignUp(request):
	return render (request, "golfApp/user-register.html")

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



def profile(request, pk):
	username = None
	if request.user.is_authenticated():
		username = request.user.username
	
	return render(request, 'golfApp/profile.html', {'profile': profile})


#Static Content:

def games(request):
        return render (request, "golfApp/other-games.html")

def rules(request):
        return render (request, "golfApp/rules.html")


	

