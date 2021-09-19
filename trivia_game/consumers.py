from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
# from asgiref.sync import async_to_sync
import json

class NewConsumers(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name= 'new_consumer'
        self.room_group_name= 'new_consumer_group'
        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
           
        )
        await self.accept()
        await  self.send(text_data=json.dumps({'status':'websocket connected'}))

    async def receive(self, text_data):
        print(text_data)

    async def disconnect(self):
        print('disconnected')

    async def ask_question(self, event):
        print(event)
        data = json.loads(event.get('value'))
        await self.send(text_data=json.dumps({'payload':data}))


    async def get_answer_choice(self, event):
        print(event)
        data = json.loads(event.get('value'))
        await self.send(text_data=json.dumps({'payload2':data}))



