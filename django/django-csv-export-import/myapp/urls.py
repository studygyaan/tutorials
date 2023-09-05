from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('', views.home, name='home'),
    path('export-csv/', views.export_csv, name='export_csv'),
    path('export-query-to-csv/', views.export_query_to_csv, name='export_query_to_csv'),
    path('export-html-to-csv/', views.export_html_to_csv, name='export_html_to_csv'),

    path('import-csv/', views.import_csv, name='import_csv'),
]
