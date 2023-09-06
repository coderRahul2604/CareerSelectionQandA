from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    detail=models.TextField()
    tags=models.TextField(default='')
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    detail=models.TextField()
    tags=models.TextField(blank=True)
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail

class Comment(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField(default='')
    add_time=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.comment[0:18]+"..."+" for "+self.answer.detail

class Like(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='like_user')
    add_time = models.DateTimeField(auto_now_add=True)

    

class Dislike(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='dislike_user')
    add_time = models.DateTimeField(auto_now_add=True)
   