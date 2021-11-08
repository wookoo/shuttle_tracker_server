from channels.generic.websocket import AsyncWebsocketConsumer
import json
import datetime

tag_dict = {
   "dae9bd80":"이승아",
    "cc1ca216":"신준용",
    "9adbb880":"이찬호",
    "fc7f2d23":"민세리",
    "dc1b7022":"이인구",
    "a99a258d":"윤재욱",
    "696bd8d" : "김기준",
    "8953ca8e":"한정우",
    "d9b1fb8d":"김도현",
}
onDrive = False
class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        global onDrive
        print("connected")
        print(datetime.datetime.now())
        print(self.scope["user"])
        self.user = self.scope['url_route']['kwargs']['user']
        self.room_group_name = 'chat_bus'


        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        
        if(self.user == "provider"):
            onDrive = True
         
            
        if(onDrive):
            await self.channel_layer.group_send(
                    
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        "user": "provider",
                        'message': {"connection":"in"}
                    }
                )
        else:
            await self.channel_layer.group_send(
                    
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        "user": "provider",
                        'message': {"connection":"out"}
                    }
                )

    async def disconnect(self, close_code):
        global onDrive

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        if(self.user == "provider"):
            onDrive = False
            await self.channel_layer.group_send(
                
                self.room_group_name,
                {
                    'type': 'chat_message',
                    "user": self.user,
                    'message': {"connection":"out"}
                }
            )

        


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        if("tag" in text_data_json.keys()):
            try:
                text_data_json['tag'] = tag_dict[text_data_json['tag']]
                await self.channel_layer.group_send(
            
                self.room_group_name,
                {
                    'type': 'chat_message',
                    "user": self.user,
                    'message': text_data_json
                }
                
            )
                return
            except:
            
                pass
        else:
            await self.channel_layer.group_send(
            
                self.room_group_name,
                {
                    'type': 'chat_message',
                    "user": self.user,
                    'message': text_data_json
                }
            )
        

        
    
        print("call Here")
        
    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        await self.send(text_data=json.dumps({
            'user' : user,
            'message': message
        }))