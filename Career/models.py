from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Career(models.Model):
    cno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    ctitle=models.CharField(max_length=100, blank=True)
    cname=models.CharField(max_length=40)
    category=models.CharField(max_length=40)
    cdetail = models.TextField(blank=True)
    tags = models.TextField(default='')
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.cname  +"|| Category==> "+ self.category

class Career2(models.Model):
    cno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    ctitle=models.CharField(max_length=100, blank=True)
    cname=models.CharField(max_length=40)
    category=models.CharField(max_length=40)
    cdetail = models.TextField()
    tags = models.TextField(default='')
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.cname  +"|| Category==> "+ self.category
