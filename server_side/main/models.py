from django.db import models

# Create your models here.
class user_data(models.Model):
    id = models.CharField(max_length = 64, primary_key=True)
    password = models.CharField(max_length = 64)
    tags = models.JSONField(default=list)

class message(models.Model):
    to = models.ForeignKey(to = user_data, on_delete = models.CASCADE)
    record_time = models.DateTimeField(auto_now=True)
    content = models.TextField()

class team(models.Model):
    members = models.ManyToManyField(to = user_data)
    title = models.TextField(default="WTF Contest")
    category = models.TextField(default="Maths")
    tags = models.JSONField(default=list)
    intro = models.TextField(default="Some nice team.")

