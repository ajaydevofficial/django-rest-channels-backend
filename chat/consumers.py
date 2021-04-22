import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["path"].split("/")[-1]
        self.room_chat_name = "chat_{}".format(self.room_name)

        # Join group
        async_to_sync(self.channel_layer.group_add)(
            self.room_chat_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_chat_name,
            self.channel_name
        )

    # Receive data to websocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        async_to_sync(self.channel_layer.group_send)(
            self.room_chat_name,
            {
                "type": "chat_message",
                "message": message
            }
        )

    # Receive message from group
    def chat_message(self,event):
        message = event["message"]

        # Send message to websocket
        self.send(text_data=json.dumps({
            "message": message
        }))
