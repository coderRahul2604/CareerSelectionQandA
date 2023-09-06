from django.contrib import admin
from django.urls import path
from Question import views as que_views

urlpatterns = [
    path('', que_views.Quehtml, name="question" ),
    path('Detailque/<int:id>', que_views.Detailque, name="Detailque" ),
    path('Detailque/add_comment/<int:id>', que_views.Detailque, name="Detailque" ),
    path('Detailque/add_comment/<int:answer_id>/', que_views.add_comment, name='add_comment'),
    path('Detailque/post_answer/<int:quest_id>/', que_views.add_answer, name='add_answer'),
    path('Detailque/save-like',que_views.save_like,name='save-upvote'),
    path('Detailque/save-dislike',que_views.save_dislike,name='save-downvote'),
 
]