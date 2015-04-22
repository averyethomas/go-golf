from django.contrib import admin
from golfApp.models import Course, coursePar, Profile, Scorecard


admin.site.register(Course)

admin.site.register(coursePar)

admin.site.register(Profile)

admin.site.register(Scorecard)