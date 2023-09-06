from django.shortcuts import render
from django.http import JsonResponse
from translate import Translator

def translator_home(request):
    return render(request, 'home.html')

def translate_text(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        target_language = request.POST.get('target_language', 'en')

        translator = Translator(to_lang=target_language)
        translation = translator.translate(text)

        response_data = {'translation': translation}
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'})
