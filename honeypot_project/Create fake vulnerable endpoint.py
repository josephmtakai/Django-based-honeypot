import logging
from django.http import HttpResponse

def fake_vulnerable_endpoint(request):
    # Simulate a vulnerable endpoint
    if request.method == 'GET':
        param = request.GET.get('param', '')
        # Log the suspicious activity
        logging.warning(f"Suspicious access with param: {param}")
        return HttpResponse(f"Echoing input: {param}")
    return HttpResponse("This endpoint is not secure.")
