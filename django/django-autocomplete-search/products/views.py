from django.http import JsonResponse
from django.views import View
from .models import Product
from django.shortcuts import render

def product_search(request):
    return render(request, 'index.html')

class ProductAutocomplete(View):
    def get(self, request):
        query = request.GET.get('term', '')
        products = Product.objects.filter(name__icontains=query)[:10]
        results = [product.name for product in products]
        return JsonResponse(results, safe=False)
