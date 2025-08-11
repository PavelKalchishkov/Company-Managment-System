import os
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diplomna_rabota.settings')  # <-- replace with your project name
django.setup()


import requests

api_key = ""
url = "http://127.0.0.1:8001/api/company/"

response = requests.get(url)
services = response.json()

print(services)



