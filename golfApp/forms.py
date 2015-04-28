from django import forms
from django.core.exceptions import ValidationError
from golfApp import models
from models import Course, Scorecard, Profile

class signup (forms.ModelForm):
	class Meta:
	      model = models.User

class locate (forms.ModelForm):
	class Meta:
	      model = models.Course

class createCourse (forms.ModelForm):
       class Meta:
              model = Course
              fields = ['name', 'address', 'MtoTprice', 'FtoSprice', 'site', 'phone', 'courseType', 'architect', 'backTees', 'backPar', 'backSlope', 'DrivingRange', 'Public', 'Private', 'Lessons', 'ClubRental', 'PuttingGreen', 'LockerRoom', 'CaddieHire', 'ProShop', 'Restaurant', 'WaterHazards', 'Bunkers', 'ParThree', 'MiniGolf', 'NineHolePlay', 'EighteenHolePlay',]

class createScorecard (forms.ModelForm):
	class Meta:
		model = Scorecard
		fields = ['date','userHole1','userHole2','userHole3','userHole4','userHole5','userHole6','userHole7','userHole8','userHole9','userHole10','userHole11','userHole12','userHole13','userHole14','userHole15','userHole16','userHole17','userHole18',]

class createProfile (forms.Form):
	Username = forms.CharField(max_length=50)
	Password = forms.CharField()