from django.urls import path
from .views import YAMLView, XMLView, JSONView

urlpatterns = [
    path('yaml/', YAMLView.as_view(), name='yaml-view'),
    path('xml/', XMLView.as_view(), name='xml-view'),
    path('json/', JSONView.as_view(), name='json-view'),
]
