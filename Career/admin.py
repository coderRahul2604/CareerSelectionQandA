from django.contrib import admin
from Career.models import Career, Career2

# Register your models here.
@admin.register(Career)
class CareerModelAdmin(admin.ModelAdmin):
    list_display=['cno','category','cname','tags', 'timeStamp']

admin.site.register(Career2)