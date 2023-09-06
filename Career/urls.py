from django.contrib import admin
from django.urls import path
from Mainproject import views as views_main
from Career import views as views_career
from Question import views as que_views

urlpatterns = [
    path('', views_career.Careerpage, name='Career'),
    path('Career_detail/<int:id>', views_career.Career_detail, name='search_career_detail_que'),


    path('askque/', views_career.askque, name='askque'),
    path('Highpaying/', views_career.Highpaying, name='Highpaying'),
    path('TopDemanded/', views_career.TopDemanded, name='TopDemanded'),
    path('Unknown/', views_career.Unknown, name='Unknown'),
    path('CareersBySubjects/', views_career.CareersBySubjects, name='CareersBySubjects'),
    path('Unique/', views_career.Unique, name='Unique'),
    path('SkillsRequired/', views_career.SkillsRequired, name='SkillsRequired'),
    path('GovernmentSector/', views_career.GovernmentSector, name='GovernmentSector'),
    path('Creative/', views_career.Creative, name='Creative'),
    path('Sports/', views_career.Sports, name='Sports'),
    path('Healthcare/', views_career.Healthcare, name='Healthcare'),
    path('Finance/', views_career.Finance, name='Finance'),
    path('IT/', views_career.IT, name='IT'),
    path('Management/', views_career.Management, name='Management'),

    path('Highpaying/Career_detail/<int:id>', views_career.Career_detail, name='Highpaying_detail'),
    path('TopDemanded/Career_detail/<int:id>', views_career.Career_detail, name='top_demanded_detail'),
    path('Unknown/Career_detail/<int:id>', views_career.Career_detail, name='Unknown_detail'),
    path('CareersBySubjects/Career_detail/<int:id>', views_career.Career_detail, name='CareersBySubjects_detail'),
    path('Unique/Career_detail/<int:id>', views_career.Career_detail, name='Unique_detail'),
    path('SkillsRequired/Career_detail/<int:id>', views_career.Career_detail, name='SkillsRequired_detail'),
    path('GovernmentSector/Career_detail/<int:id>', views_career.Career_detail2, name='GovernmentSector_detail'),
    path('Creative/Career_detail/<int:id>', views_career.Career_detail2, name='Creative_detail'),
    path('Sports/Career_detail/<int:id>', views_career.Career_detail2, name='Sports_detail'),
    path('Healthcare/Career_detail/<int:id>', views_career.Career_detail, name='Healthcare_detail'),
    path('Finance/Career_detail/<int:id>', views_career.Career_detail, name='Finance_detail'),
    path('IT/Career_detail/<int:id>', views_career.Career_detail, name='IT_detail'),
    path('Management/Career_detail/<int:id>', views_career.Management, name='Management_detail'),

]