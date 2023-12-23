from django.http.response import HttpResponse
from django.shortcuts import render

def profile_request(request):
    return render(request, "netflixapp/profile.html")

def entry_request(request):
    return render(request, "netflixapp/entry.html")