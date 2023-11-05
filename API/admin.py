from django.contrib import admin
from .models import *

# Register your models here.

class StudentResultView(admin.ModelAdmin):
    list_display = ['id', 'username', 'subject', 'marks']

admin.site.register(StudentResults, StudentResultView)