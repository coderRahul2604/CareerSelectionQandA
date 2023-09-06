from django.contrib import admin
from django.urls import path
from Mainproject import views as views_main

urlpatterns = [
    path('', views_main.index, name='index'),
    path('About', views_main.About, name='About'),
    path('Login', views_main.Login, name='Login'),
    path('Logout', views_main.Logout, name='Logout'),
    path('Signup', views_main.Signup, name='Signup'),
    path('Signup', views_main.Signup, name='Signup'),
    path('ikigai', views_main.ikigai, name='ikigai'),
    path('profile/<str:username>', views_main.profile, name='profile'),
    path('report', views_main.report, name='report'),
    #path('Main_report', views_main.Main_report, name='Main_report'),
    path('Question_report', views_main.Question_report, name='Question_report'),
    path('Answer_report', views_main.Answer_report, name='Answer_report'),
    path('Comment_report', views_main.Comment_report, name='Comment_report'),
    path('Profile_report', views_main.Profile_report, name='profile_report'),
    path('Like_report', views_main.Like_report, name='Like_report'),
    path('Dislike_report', views_main.Dislike_report, name='Dislike_report'),
    
    path('forgotpass', views_main.forgotpassword, name='forgotpass'),
    
    path('Askquestion', views_main.Askquestion, name='Askquestion'),
    
]