from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'mini-home'),
    path('about/',views.about, name = 'mini-about'),
    path('help/',views.help, name = 'mini-help'),
    path('visual/', views.visual, name = 'mini-visual'),
    path('main/', views.main, name = 'mini-main'),
    path('traveller/', views.traveller, name = 'mini-traveller'),
    path('travel/', views.travel, name = 'mini-travel'),
    path('helpstudent/', views.helpstudent, name = 'mini-helpstudent'),
    path('student', views.student, name = 'mini-student')
    # path('main/', views.main, name = 'mini-main') 
]
