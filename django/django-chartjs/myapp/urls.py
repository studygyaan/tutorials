from django.urls import path
from . import views

urlpatterns = [
    path('chart-data/', views.chart_data, name='chart_data'),
    path('chart/', views.chart_view, name='chart_view'),
]