from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "netflixclone/index.html")

def signup(request):
    return render(request, "netflixclone/registration/signup.html")

def latest(request):
    return render(request, "netflixclone/latest.html")

def latest_details(request, id):
    return render(request, "netflixclone/latest-details.html", {
        "id": id
    })
