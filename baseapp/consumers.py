import json
from channels.generic.websocket import WebsocketConsumer
from .dbfunctions import *


class ChatConsumer(WebsocketConsumer):

    old_response = ""


    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            "type":"connection_established",
            "message":"Connected!"
        }))

    def receive(self, text_data):

            message = json.loads(text_data)["message"]
            
            returned_data = handle_request(self.old_response,message)
        
            response = returned_data["response_text"]
            self.old_response = response
            

            self.send(text_data=json.dumps({
                "type":"chat-user",
                "message":message
            }))

            self.send(text_data=json.dumps({
                "type":"chat-bot",
                "message":response
            }))