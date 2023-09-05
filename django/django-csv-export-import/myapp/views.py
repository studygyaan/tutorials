from django.http import HttpResponse
from django.shortcuts import render
import csv
from bs4 import BeautifulSoup
from .models import Person


def home(request):
    return render(request, 'home.html')


def export_csv(request):
    # Your data retrieval logic goes here
    data = [
        ['Name', 'Age', 'Email'],
        ['John Doe', 30, 'john@example.com'],
        ['Jane Smith', 25, 'jane@example.com'],
        # Add your data here
    ]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'

    writer = csv.writer(response)
    for row in data:
        writer.writerow(row)

    return response


def export_query_to_csv(request):
    data = Person.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="people.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Age', 'Email'])  # CSV header

    for person in data:
        writer.writerow([person.name, person.age, person.email])

    return response


def export_html_to_csv(request):
    html = """
    <!-- Your HTML table content here -->
    """
    soup = BeautifulSoup(html, 'html.parser')
    data = []

    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        data.append([col.text for col in cols])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="/table_data.csv"'

    writer = csv.writer(response)
    for row in data:
        writer.writerow(row)

    return response


# views.py
from django.shortcuts import render, redirect
from .forms import CSVImportForm
from .models import Book
import csv

def import_csv(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                Book.objects.create(
                    title=row['title'],
                    author=row['author'],
                    publication_year=row['publication_year'],
                    isbn=row['isbn']
                )

            return redirect('home')  # Redirect to a success page
    else:
        form = CSVImportForm()
    
    return render(request, 'import.html', {'form': form})
