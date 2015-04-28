from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	latlon = models.CharField('Geocoordinates', max_length=50, blank=True, null=True)
	MtoTprice = models.CharField('Weekday Price', max_length=50)
	FtoSprice = models.CharField('Weekend Price',max_length=50)
	site = models.CharField('Website',max_length=50)
	phone = models.CharField(max_length=50, null=True)
	courseType = models.CharField(max_length=50, null=True)
	architect = models.CharField(max_length=50, null=True)
	backTees = models.IntegerField(unique=False, null=True)
	backPar = models.IntegerField(unique=False, null=True)
	backSlope = models.IntegerField(unique=False, null=True)
	DrivingRange = models.BooleanField(default=False, blank=True)
	Public = models.BooleanField(default=False, blank=True)
	Private = models.BooleanField(default=False, blank=True)
	Lessons = models.BooleanField(default=False, blank=True)
	ClubRental = models.BooleanField(default=False, blank=True)
	PuttingGreen = models.BooleanField(default=False, blank=True)
	LockerRoom = models.BooleanField(default=False, blank=True)
	CaddieHire = models.BooleanField(default=False, blank=True)
	ProShop = models.BooleanField(default=False, blank=True)
	Restaurant = models.BooleanField(default=False, blank=True)
	WaterHazards = models.BooleanField(default=False, blank=True)
	Bunkers = models.BooleanField(default=False, blank=True)
	ParThree = models.BooleanField(default=False, blank=True)
	MiniGolf = models.BooleanField(default=False, blank=True)
	NineHolePlay = models.BooleanField(default=False, blank=True)
	EighteenHolePlay = models.BooleanField(default=False, blank=True)
	
	class Meta(object):
		verbose_name_plural = "Courses"
	def __unicode__(self):
		return unicode (self.name)
	def save(self, *args, **kwargs):
		super(Course, self).save(*args, **kwargs)


class Profile(models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField("photos", blank = True, null = True)
	hometown = models.CharField(max_length=50)
	state = models.CharField(max_length=2)
	birthdate = models.DateField(null=True, blank=True)
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	email = models.CharField(max_length=75)
	phone = models.CharField(max_length=15, blank = True, null = True)
	
	class Meta(object):
		verbose_name_plural = "Profiles"
	def __unicode__(self):
		return unicode (self.user)
	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

class coursePar(models.Model):
	course = models.OneToOneField(Course)
	hole1 = models.IntegerField(blank=True, null=True)
	hole2 = models.IntegerField(blank=True, null=True)
	hole3 = models.IntegerField(blank=True, null=True)
	hole4 = models.IntegerField(blank=True, null=True)
	hole5 = models.IntegerField(blank=True, null=True)
	hole6 = models.IntegerField(blank=True, null=True)
	hole7 = models.IntegerField(blank=True, null=True)
	hole8 = models.IntegerField(blank=True, null=True)
	hole9 = models.IntegerField(blank=True, null=True)
	hole10 = models.IntegerField(blank=True, null=True)
	hole11 = models.IntegerField(blank=True, null=True)
	hole12 = models.IntegerField(blank=True, null=True)
	hole13 = models.IntegerField(blank=True, null=True)
	hole14 = models.IntegerField(blank=True, null=True)
	hole15 = models.IntegerField(blank=True, null=True)
	hole16 = models.IntegerField(blank=True, null=True)
	hole17 = models.IntegerField(blank=True, null=True)
	hole18 = models.IntegerField(blank=True, null=True)
	
	def parTotal(self):
		return self.hole1+hole2+hole3+hole4+hole5+hole6+hole7+hole8+hole9+hole10+hole11+hole12+hole13+hole14+hole15+hole16+hole17+hole18

	def parTotalNine(self):
		return self.hole1+hole2+hole3+hole4+hole5+hole6+hole7+hole8+hole9	
	
	class Meta(object):
		verbose_name_plural = "coursePars"
	
	def __unicode__(self): 
		return unicode (self.id)
	
	def save(self, *args, **kwargs):
		super(coursePar, self).save(*args, **kwargs)

class Scorecard(models.Model):
	user = models.ForeignKey(User)
	course = models.ForeignKey(Course)
	date = models.DateField(null=True, blank=True)
	userHole1 = models.IntegerField(blank=True, null=True)
	userHole2 = models.IntegerField(blank=True, null=True)
	userHole3 = models.IntegerField(blank=True, null=True)
	userHole4 = models.IntegerField(blank=True, null=True)
	userHole5 = models.IntegerField(blank=True, null=True)
	userHole6 = models.IntegerField(blank=True, null=True)
	userHole7 = models.IntegerField(blank=True, null=True)
	userHole8 = models.IntegerField(blank=True, null=True)
	userHole9 = models.IntegerField(blank=True, null=True)
	userHole10 = models.IntegerField(blank=True, null=True)
	userHole11 = models.IntegerField(blank=True, null=True)
	userHole12 = models.IntegerField(blank=True, null=True)
	userHole13 = models.IntegerField(blank=True, null=True)
	userHole14 = models.IntegerField(blank=True, null=True)
	userHole15 = models.IntegerField(blank=True, null=True)
	userHole16 = models.IntegerField(blank=True, null=True)
	userHole17 = models.IntegerField(blank=True, null=True)
	userHole18 = models.IntegerField(blank=True, null=True)

	def userTotal(self):
		return self.userHole1+userHole2+userHole3+userHole4+userHole5+userHole6+userHole7+userHole8+userHole9+userHole10+userHole11+userHole12+userHole13+userHole14+userHole15+userHole16+userHole17+userHole18

	def userTotalNine(self):
		return self.userHole1+userHole2+userHole3+userHole4+userHole5+userHole6+userHole7+userHole8+userHole9	

	class Meta(object):
		verbose_name_plural = "Scorecards"
	
	def __unicode__(self):
		return unicode (self.id)
	
	def save(self, *args, **kwargs):
		super(Scorecard, self).save(*args, **kwargs)
