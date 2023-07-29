from django.shortcuts import render
from django.http import HttpResponse
from django_pandas.io import read_frame
from .models import Employee
import pandas as pd

def hello_world(request):
    return HttpResponse("Hello, world!")

# Example: Django QuerySet to Pandas DataFrame
def employees_data(request):
    # Retrieve all employees from the database using Django QuerySet
    queryset = Employee.objects.all()

    # Convert the QuerySet to a Pandas DataFrame
    employees_df = read_frame(queryset)

    return render(request, 'employees_data.html', {'employees_df': employees_df})

# Example: Pandas DataFrame to Django Model
def save_employees_data(request):
    # Sample data in a Pandas DataFrame
    data = {
        'name': ['John', 'Alice', 'Bob'],
        'age': [30, 25, 28],
        'department': ['HR', 'Finance', 'Engineering'],
        'salary': [50000.00, 60000.00, 55000.00],
    }

    employees_df = pd.DataFrame(data)

    # Convert the DataFrame to Django Model instances and save them
    for index, row in employees_df.iterrows():
        Employee.objects.create(
            name=row['name'],
            age=row['age'],
            department=row['department'],
            salary=row['salary']
        )

    return render(request, 'success.html')

# Example: Pandas DataFrame to HTML Table
def display_table(request):
    # Sample data in a Pandas DataFrame
    data = {
        'name': ['John', 'Alice', 'Bob'],
        'age': [30, 25, 28],
        'department': ['HR', 'Finance', 'Engineering'],
        'salary': [50000.00, 60000.00, 55000.00],
    }

    employees_df = pd.DataFrame(data)

    # Convert the DataFrame to an HTML table
    html_table = employees_df.to_html()

    return render(request, 'display_table.html', {'html_table': html_table})


