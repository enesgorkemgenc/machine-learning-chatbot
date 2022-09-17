# machine-learning-chatbot

> A chatbot that learns to answer through chatting.

## Demo GIF

![mlchatbotdemogif](https://user-images.githubusercontent.com/93938698/190865693-2b15bc83-e4b4-41f0-88ea-3ba2d7e4967b.gif)

## How does it work ?

![mlchatbotlogic](https://user-images.githubusercontent.com/93938698/190812135-2a7c4626-c48e-43ba-a0b3-545288213d0d.png)


there is old_message, and the new_message text that entered by user.

filter new_message

if filtered new message is not appropriate:
	
	return a random message that has no recorded response


save the new_message as a response of old_message

if new_message has any response:

    return a random response of new_message

else:

      return a random message that has no response

  
## Technologies I used

- HTML, CSS, JavaScript
- Python, Django, Django Channels
  
  
