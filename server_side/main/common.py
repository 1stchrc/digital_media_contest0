from . import models
from channels.db import database_sync_to_async as s2a

def auth(req_json):
    users = models.user_data.objects.filter(id = req_json["user_id"])
    if users.exists():
        return users[0]
    return None