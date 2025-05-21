from django.db import models

class PostModel(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    faculty=models.CharField(max_length=255)
    age=models.IntegerField()
