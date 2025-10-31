from django.http import HttpResponse
from django.shortcuts import render
import requests

# 1. Home Page
def home(request):
    return HttpResponse("<h2>Welcome to the Home Page</h2>")

# 2. About Page
def about(request):
    return HttpResponse("<h2>About Us: This is a simple Django app</h2>")

# 3. Contact Page
def contact(request):
    return HttpResponse("<h2>Contact Us at info@example.com</h2>")

# 4. Services Page
def services(request):
    return HttpResponse("<h2>Our Services: Web Development, AI Integration, and Cloud Solutions</h2>")

# 5. Portfolio Page
def portfolio(request):
    return HttpResponse("<h2>Check out our past projects and case studies!</h2>")

# 6. Team Page
def team(request):
    return HttpResponse("<h2>Meet Our Awesome Team Members</h2>")

# 7. Blog Page
def blog(request):
    return HttpResponse("<h2>Welcome to our daverze! New posts coming soon.</h2>")

# 8. API Data Example (uses the 'requests' library)
def api_data(request):
    try:
        response = requests.get("https://api.github.com")
        data = response.json()
        return HttpResponse(f"<h3>GitHub API status: {data['current_user_url']}</h3>")
    except Exception as e:
        return HttpResponse(f"<h3>Error fetching API: {e}</h3>")
