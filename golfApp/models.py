from django.db import models

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


