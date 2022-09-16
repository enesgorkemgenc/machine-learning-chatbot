import json
from channels.generic.websocket import WebsocketConsumer
from . import methods, models

class ChatConsumer(WebsocketConsumer):

    old_response = None


    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            "type":"connection_established",
            "message":"Connected!"
        }))

    def receive(self, text_data):

        message_text = json.loads(text_data)["message"]
        
        response = methods.handle_chat(self.old_response, message_text)

        self.old_response = response

        self.send(text_data=json.dumps({
            "type":"chat-bot",
            "message":response.content
        }))