from django.shortcuts import render, redirect
from .forms import EventForm

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Replace 'event_list' with your desired redirect URL after successful form submission
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})