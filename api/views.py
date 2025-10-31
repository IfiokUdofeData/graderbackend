from django.http import HttpResponse
from django.shortcuts import render
# import requests

# Function 1 — Home Page
def home(request):
    return HttpResponse("<h2>Welcome to the Home Page</h2>")

# Function 2 — About Page
def about(request):
    return HttpResponse("<h2>About Us: This is a simple Django app</h2>")

# Function 3 — Contact Page
def contact(request):
    return HttpResponse("<h2>Contact Us at info@example.com</h2>")
