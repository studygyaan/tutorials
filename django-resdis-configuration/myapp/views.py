from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!")

# views.py

import random
from django.shortcuts import render
from django.core.cache import cache
from time import sleep

def time_consuming_task():
    # Simulating a time-consuming task by generating a random number between 1 and 100
    sleep(5)
    return random.randint(1, 100)

def cached_view(request):
    # Check if the result is already in the cache
    result = cache.get('cached_result')
    if result is None:
        # If not in cache, perform the time-consuming task and store the result in cache
        result = time_consuming_task()
        cache.set('cached_result', result, timeout=30)  # Cache result for 30 seconds

    return render(request, 'cached_view.html', {'result': result})
