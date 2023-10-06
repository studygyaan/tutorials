# your_app_name/tasks.py
from django.core.management.base import BaseCommand
from datetime import datetime

def sample_task():
    """
    This is a sample task function that you can schedule to run periodically.
    In this example, we'll simply print a message and log the current date and time.
    """

    # You can replace this with your actual task logic
    print("Sample task is running at:", datetime.now())

    # Add your task logic here
    # For example, you could update database records, send emails, generate reports, etc.

# Additional task functions can be defined here if needed
