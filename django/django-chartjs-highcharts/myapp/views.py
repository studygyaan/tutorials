from django.shortcuts import render
from django.http import JsonResponse
from .models import ChartData

def chart_data(request):
    data = ChartData.objects.all()
    labels = [item.label for item in data]
    values = [item.value for item in data]
    
    chart_data = {
        'label': 'Line Chart',
        'labels': labels,
        'values': values,
        'chart_type': 'bar'
    }
    
    return JsonResponse(chart_data)

def chart_view(request):
    return render(request, 'chart.html')