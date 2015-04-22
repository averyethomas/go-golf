from django.conf.urls import patterns, include, url
from django.contrib import admin
from golfApp import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    
    # Gets User Location and List Courses: 
    #url(r'^locate$', views.locate, name='locate'),
    
    # Course Related:
    url(r'^courses$', views.courseList, name='course-list'),
    #url(r'^courses/(?P,<pk>\d+)$', views.course, name='course'),
    url(r'^courses/add-course$', views.formCourse, name='add-course'),
    
    #Profile Related: 
    
    #url(r'^users/(?P<pk>\d+)$', views.userProfile, name='userProfile'),
    #url(r'^user-signup$', views.userSignUp, name='userSignUp'),
    url(r'^user-login$', views.userLogin, name='user-login'),
    url(r'^user-logout$', views.userLogout, name='user-logout'),
    #url(r'^friends$', views.profileList, name='profileList'),
    
    #Scorecard Related: 
    #url(r'^scorecards$', views.scorecardsList, name='scorecardsList'),
    #url(r'^scorecards/(?P,<pk>\d+)$', views.scorecard, name='scorecard'),
    #url(r'^scorecards/add-scorecard$', views.formScorecard, name='form_scorecard'),
    
    #Admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #Static Pages:
    url(r'^rules$', views.rules, name='rules'),
    url(r'^more-games$', views.games, name='more-games'),
)
