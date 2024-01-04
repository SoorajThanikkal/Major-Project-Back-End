from django.test import TestCase
import requests

url = 'http://127.0.0.1:8000/auth/clients-create/'
headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA0MzQ5MTY0LCJpYXQiOjE3MDQzNDg1NjQsImp0aSI6ImM3NDRkODdlZmYxMjQ4Y2E4ODhjY2IzYTg5YzY1NWJjIiwidXNlcl9pZCI6MTB9.bcY30dj3t9Sf_fU_--8B8XIh9s5Y--RQSy3Gbr0HEWI'}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())

# Create your tests here.
