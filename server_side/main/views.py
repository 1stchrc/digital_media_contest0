from django.shortcuts import render
from django.http import *
from . import models
import json
from .consumers import connected_users
from .common import *
from asgiref.sync import async_to_sync as a2s

# Create your views here.
def post_message(req):
    req_json = json.loads(req.body)
    users = models.user_data.objects.filter(id = req_json["to"])
    if not users.exists():
        return HttpResponseNotFound("User doesn't exist.")
    msg = models.message()
    user = users[0]
    msg.to = user
    msg.content  = req_json["content"]
    msg.save()
    a2s(connected_users[user.id].send)(json.dumps({"type" : "MESSAGE", "data" : msg.id}))
    return HttpResponse("ok")

def register(req):
    req_json = json.loads(req.body)
    mail = req_json["mail"]
    if models.user_data.objects.filter(id = mail).exists():
        return HttpResponseForbidden("User already exists.")
    user = models.user_data()
    user.id = mail
    user.name = req_json["username"]
    user.password = req_json["password"]
    user.save()
    return HttpResponse("Success.")

def create_team(req):
    req_json = json.loads(req.body)
    user = auth(req_json["user_info"])
    if user == None:
        return HttpResponseNotFound("Authentication failed.")
    team = models.team()
    team.title = req_json["title"]
    team.intro = req_json["intro"]
    team.leader_id = user.id
    team.members.add(user)
    team.save()
    return HttpResponse(str(team.id))

def post(req):
    req_json = json.loads(req.body)
    user = auth(req_json["user_info"])
    if user == None:
        return HttpResponseNotFound("Authentication failed.")
    post = models.post()
    post.author_id = user.id
    post.title = req_json["title"]
    post.content = req_json["content"]
    post.tags = req_json["tags"]
    post.private_flag = req_json["private_flag"]
    post.save()
    return HttpResponse(str(post.id))

def fetch_posts(req):
    cnt = int(req.GET.get("post_count"))
    counter = 0
    ret = []    
    for e in models.post.objects.all():
        if counter >= cnt:
            break
        counter += 1
        ret.append({"title":e.title, "content":e.content, "tags":e.tags})
    return HttpResponse(json.dumps(ret))