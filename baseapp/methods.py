from .models import Message
import random


def handle_chat(old_response ,new_message_text):
    new_message_text = "".join([char for char in new_message_text if char.isalnum() or char in " ?!:(),."]).strip().lower()

    if len(new_message_text) < 2:
        
        return Message.get_random_unanswered_message()

    new_message, created = Message.objects.get_or_create(content=new_message_text)

    if old_response:
        old_response.add_response(new_message)

    if new_message.responses.all().exists():
        
        return new_message.get_random_response()
        
    else:

        #to prevent chatbot to reply with the same message when the message is created recently

        response = Message.get_random_unanswered_message()

        if response == new_message:
            response = random.choice(Message.objects.all())

        return response
    