from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect
from golfApp.models import Course, coursePar, Profile, Scorecard
from datetime import datetime
from django.contrib import auth

def home(request):
	return render(request, "base.html")

#Courses Based on Location:

def locate(request):
	return 




#Static Content:
def games(request):
        return render (request, "games.html")

def rules(request):
        return render (request, "rules.html")
