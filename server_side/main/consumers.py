import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from channels.db import database_sync_to_async as s2a
from . import models
from .common import *
import asyncio
import time
connected_users = dict()

class UserConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, msg):
        await self.accept()
        async def discard_async(time):
            await asyncio.sleep(time)
            await self.close()
        self.future_discard = asyncio.create_task(discard_async(5))

    async def websocket_receive(self, event):
        async def discard_async_loop():
            while True:
                cur_time = time.time()
                if cur_time >= self.discard_time:
                    await self.close()
                    return
                await asyncio.sleep(self.discard_time - cur_time)
        self.discard_time = time.time() + 180
        try:
            msg = json.loads(event["text"])
            if msg["type"] == "BEGIN":
                try:
                    self.future_discard.cancel()
                    del self.future_discard
                    user = await s2a(auth)(msg["data"])
                    if user == None:
                        print("Bad request.")
                        await self.send(json.dumps({"type" : "REJECT", "data" : {}}))
                        await self.close()
                        return
                    self.user_id = user.id
                    connected_users[user.id] = self
                    asyncio.create_task(discard_async_loop())
                    await self.send(json.dumps({"type" : "BEGIN", "data" : {
                        "user_id": user.id,
                        "name": user.name,
                        "tags": json.dumps(user.tags),
                    }}))
                    print(f"User connected: {user.id}")
                except:
                    await self.close()
        except:
            pass

    async def websocket_disconnect(self, msg):
        if hasattr(self, "user_id"):
            del connected_users[self.user_id]
            print("User disconnected: " + self.user_id)
        raise StopConsumer()