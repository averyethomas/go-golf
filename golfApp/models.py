from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
	courseID = models.IntegerField(blank=True, null=True)
	name = models.CharField(max_length=50)
	street = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zipcode = models.CharField(max_length=50)
	latlon = models.CharField(max_length=50)
	MtoTprice = models.CharField(max_length=50)
	FtoSprice = models.CharField(max_length=50)
	site = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
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
		return unicode (self.courseID)
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
	
	class Meta(object):
		verbose_name_plural = "Profiles"
	def __unicode__(self):
		return unicode (self.useriD)
	def save(self, *args, **kwargs):
		super(User, self).save(*args, **kwargs)

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

	class Meta(object):
		verbose_name_plural = "coursePars"
	def __unicode__(self): 
		return self.name
	
	def save(self, *args, **kwargs):
		super(coursePar, self).save(*args, **kwargs)

class Scorecard(models.Model):
	user = models.ForeignKey(User)
	coursePar = models.ForeignKey(coursePar)
	course = models.ForeignKey(Course)
	1hole = models.IntegerField(blank=True, null=True)
	2hole = models.IntegerField(blank=True, null=True)
	3hole = models.IntegerField(blank=True, null=True)
	4hole = models.IntegerField(blank=True, null=True)
	5hole = models.IntegerField(blank=True, null=True)
	6hole = models.IntegerField(blank=True, null=True)
	7hole = models.IntegerField(blank=True, null=True)
	8hole = models.IntegerField(blank=True, null=True)
	9hole = models.IntegerField(blank=True, null=True)
	10hole = models.IntegerField(blank=True, null=True)
	11hole = models.IntegerField(blank=True, null=True)
	12hole = models.IntegerField(blank=True, null=True)
	13hole = models.IntegerField(blank=True, null=True)
	14hole = models.IntegerField(blank=True, null=True)
	15hole = models.IntegerField(blank=True, null=True)
	16hole = models.IntegerField(blank=True, null=True)
	17hole = models.IntegerField(blank=True, null=True)
	18hole = models.IntegerField(blank=True, null=True)

	class Meta(object):
		verbose_name_plural = "Scorecards"
	def __unicode__(self):
		return self.name
	def save(self, *args, **kwargs):
		super(Scorecard, self).save(*args, **kwargs)
