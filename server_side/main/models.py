from django.db import models

# Create your models here.
class user_data(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    tags = models.JSONField(default=list)

class message(models.Model):
    to = models.ForeignKey(to = user_data, on_delete = models.CASCADE)
    record_time = models.DateTimeField(auto_now=True)
    content = models.TextField()

class team(models.Model):
    leader_id = models.CharField(max_length=64)
    members = models.ManyToManyField(user_data)
    title = models.TextField(default="WTF Contest")
    #category = models.TextField(default="Maths")
    #tags = models.JSONField(default=list)
    positions = models.JSONField(default=dict)

class post_reply(models.Model):
    content = models.TextField(default="Nice reply.")
    author = models.ForeignKey(to = "post", default="", on_delete=models.SET_NULL, null = True)

class post(models.Model):
    title = models.TextField(default="Nice post.")
    content = models.TextField(default="Some content...")
    author = models.ForeignKey(to=user_data, null=True, on_delete=models.SET_NULL)
    tags = models.JSONField(default=list)
    private_flag = models.BooleanField(default=False)
    replies = models.ManyToManyField(to = post_reply)