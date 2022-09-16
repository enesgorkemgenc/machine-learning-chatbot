from django.db import models
import random


class Message(models.Model):

    content = models.CharField(max_length=200)

    responses = models.ManyToManyField("Message", related_name="requests", blank=True)

    random_weights_text = models.TextField(null=True, blank=True, default="")


    def __str__(self):

        return self.content[:30]


    def add_response(self, message):
        
        self.responses.add(message)
        self.random_weights_text += f"{message.id} "
        self.save()


    def get_random_response(self):

        all_responses = self.responses.all()
        id_list = self.random_weights_text.strip().split()

        random_weights = [id_list.count(str(response.id)) for response in all_responses]

        return random.choices(all_responses, weights=random_weights, k=1)[0]

    
    def get_random_unanswered_message():

        all_unanswered_messages = Message.objects.filter(responses=None)

        return random.choice(all_unanswered_messages)
