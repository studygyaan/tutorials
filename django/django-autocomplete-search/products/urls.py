from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_search, name='product-search'),
    path('autocomplete/', views.ProductAutocomplete.as_view(), name='product-autocomplete'),
]