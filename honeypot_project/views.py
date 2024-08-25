from django.shortcuts import render
from django.http import HttpResponse
import logging

# Set up logging
logger = logging.getLogger(__name__)

def fake_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Log the attempted credentials
        logger.warning(f"Attempted login with username: {username} and password: {password}")
        return HttpResponse("Login failed. Please try again.")
    return render(request, 'honeypot/fake_login.html')
