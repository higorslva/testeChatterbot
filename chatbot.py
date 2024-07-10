from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('BotBoladão')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.portuguese")

pergunta = input('Me faça uma pergunta: ')
response = chatbot.get_response(pergunta)

print(response)
