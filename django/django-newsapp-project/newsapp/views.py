from django.shortcuts import render
from newsapi import NewsApiClient
from .forms import NewsFilterForm

def news_list(request):
    api_key = 'cadbc2508df2455eaac5c72e19d342c9'  # Replace with your News API key
    newsapi = NewsApiClient(api_key=api_key)

    # Default values for country and category
    country = 'us'
    category = 'general'

    if request.method == 'GET':
        form = NewsFilterForm(request.GET)
        if form.is_valid():
            country = form.cleaned_data['country']
            category = form.cleaned_data['category']

    # Fetch news articles based on user selections
    articles = newsapi.get_top_headlines(country=country, category=category, page_size=10)

    return render(request, 'news_list.html', {'articles': articles['articles'], 'form': form})
