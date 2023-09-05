from django.shortcuts import render
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Product

def hello_world(request):
    return HttpResponse("Hello, world!")

def export_to_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="products.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.title = "Products"

    # Add headers
    headers = ["Name", "Price", "Quantity"]
    ws.append(headers)

    # Add data from the model
    products = Product.objects.all()
    for product in products:
        ws.append([product.name, product.price, product.quantity])

    # Save the workbook to the HttpResponse
    wb.save(response)
    return response
