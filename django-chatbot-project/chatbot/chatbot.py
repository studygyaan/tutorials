from chatterbot import ChatBot
import spacy

spacy.cli.download("en_core_web_sm")
spacy.cli.download("en")

nlp = spacy.load('en_core_web_sm')

chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training With Own Questions 
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

import os

# Get the base directory of your Django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct the paths to the data files
training_data_quesans_path = os.path.join(BASE_DIR, 'training_data', 'ques_ans.txt')
training_data_personal_path = os.path.join(BASE_DIR, 'training_data', 'personal_ques.txt')

# Open and read the data files
training_data_quesans = open(training_data_quesans_path).read().splitlines()
training_data_personal = open(training_data_personal_path).read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer.train(training_data)

# Training With Corpus
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer_corpus = ChatterBotCorpusTrainer(chatbot)

trainer_corpus.train(
    'chatterbot.corpus.english'
)