from django.db import models
# Create your models here.

class StudentResults(models.Model):
    username = models.TextField()
    subject = models.TextField()
    marks = models.TextField()