from django.contrib import admin
from Mainproject.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user']