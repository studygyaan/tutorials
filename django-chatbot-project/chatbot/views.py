from django.shortcuts import render
from .chatbot import chatbot

def chatbot_home(request):
    return render(request, 'index.html')

from django.http import HttpResponse
from chatterbot import ChatBot

def get_response(request):
    user_input = request.GET.get('msg')
    response = chatbot.get_response(user_input)
    return HttpResponse(str(response))

