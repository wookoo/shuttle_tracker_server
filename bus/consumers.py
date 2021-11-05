from channels.generic.websocket import AsyncWebsocketConsumer
import json
import datetime
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connected")
        print(datetime.datetime.now())
   
        self.room_name = "bus"
        self.room_group_name = 'chat_bus'


        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': "호스트가 이탈했습니다."
            }
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
    

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': text_data_json
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))