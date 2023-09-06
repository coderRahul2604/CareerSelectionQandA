from django.contrib import admin
from Question.models import Question, Answer, Comment, Like, Dislike
# Register your models here.

@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'title','tags', 'add_time']

@admin.register(Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display=['id','question', 'user','tags', 'add_time']

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'add_time']

@admin.register(Like)
class LikeModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user']

@admin.register(Dislike)
class DisLikeModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user']

