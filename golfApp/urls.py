from django.conf.urls import patterns, include, url
from django.contrib import admin
from golfApp import views

urlpatterns = patterns('',
    # Home:
    url(r'^$', views.home, name='home'),
    
    # Course Related:
    url(r'^courses$', views.courseList, name='course-list'),
    url(r'^courses/(?P<pk>\d+)$', views.course, name='course'),
    url(r'^courses/add-course$', views.formCourse, name='add-course'),
    url(r'^locate$', views.locate, name='locate'),
    
    #Profile Related: 
    
    #url(r'^register$', views.register, name='register'),
    url(r'^user-login$', views.userLogin, name='user-login'),
    url(r'^user-logout$', views.userLogout, name='user-logout'),
    
    #Scorecard Related: 
    url(r'^scorecards$', views.scorecards_list, name='scorecards-list'),
    url(r'^scorecards/(?P<pk>\d+)$', views.scorecard, name='scorecard'),
    url(r'^scorecards/add-scorecard$', views.formScorecard, name='form_scorecard'),
    
    #Admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #Static Pages:
    url(r'^more-games$', views.games, name='more-games'),
)
