from django.contrib import admin
from .models import Singer,Song
# Register your models here.

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display=['id','name','gender']

@admin.register(Song)
class Song(admin.ModelAdmin):
    list_display=['id','title','singer','duration']
