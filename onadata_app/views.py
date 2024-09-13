from django.shortcuts import render
import requests
from django.http import HttpResponse

BASE_URL = 'https://api.ona.io/api/v1/forms'


def form_data(request, form_id):
    try:
        url = f"{BASE_URL}/{form_id}"
        response = requests.get(url)

        if response.status_code == '200':
            data = response.json()
            return render(request, 'index.html', {'data': data})
        else:
            return HttpResponse(f"Error: Form id {form_id} not found or API Error")
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Network Error: {str(e)}", status=500)
