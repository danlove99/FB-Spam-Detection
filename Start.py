from fbchat import log, Client
import random	
import getpass
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from SMS import predict

class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        
        if author_id != self.uid:
            Spam = predict(message_object.text)
            if Spam == 'spam':
                message_object.text = 'Go away spammer!'
            else:
                pass
	        self.send(message_object, thread_id=thread_id, thread_type=thread_type)
	        	
if __name__ == '__main__':
    email = input('Email:')
    password = getpass.getpass()
    client.listen()