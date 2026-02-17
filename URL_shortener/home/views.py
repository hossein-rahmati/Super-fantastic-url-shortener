from django.conf import settings
from django.shortcuts import render, redirect
import requests


# Create your views here.
def index(request):
    return render(request, "home/index.html")


def index_form(request):
    if request.method == "POST":
        long_url = request.POST.get("long_url")
        shortened_url = shorten_url(long_url)
        return render(request, "home/new_url.html", {"shortened_url": shortened_url})
    return redirect("index")


def shorten_url(long_url):
    url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {settings.BITLY_TOKEN}",
    }
    data = {
        "long_url": long_url,
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["link"]
    else:
        return "Error shortening URL"
