from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gogolf.views.home', name='home'),
    
    # Gets User Location and List Courses: 
    url(r'^locate$', views.locate, name='locate'),
    
    # Course Related:
    url(r'^courses$', views.courseList, name='courseList'),
    url(r'^courses/(?P,<pk>\d+)$', views.course, name='course'),
    url(r'^courses/add_course$', views.formCourse, name='form_course'),
    
    #Profile Related: 
    
    url(r'^users/(?P<pk>\d+)$', views.userProfile, name='userProfile'),
    url(r'^user_signup$', views.userSignUp, name='userSignUp'),
    url(r'^user_login$', views.userLogin, name='userLogin'),
    url(r'^friends$', views.profileList, name='profileList'),
    
    #Scorecard Related: 
    url(r'^scorecards$', views.scorecardsList, name='scorecardsList'),
    url(r'^scorecards/(?P,<pk>\d+)$', views.scorecard, name='scorecard'),
    url(r'^scorecards/add_scorecard$', views.formScorecard, name='form_scorecard'),
    
    #Admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #Static Pages:
    url(r'^rules$', views.rules, name='rules'),
    url(r'^more_games$', views.games, name='games'),
)
