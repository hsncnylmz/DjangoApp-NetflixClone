from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect("latest")
        else:
            return render(request, "account/login.html", {
                "error": "E-posta veya Telefon Numarası yanlış"
            })
            
    return render(request, "account/login.html")

def stepone(request):
    return render(request, 'account/stepone.html')

def steptwo_request(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "account/steptwo.html", {"error": "Bu kullanıcı adı daha önceden kullanılmış"})
        else:
            user = User.objects.create_user(username=username, password=password)
            # Otomatik giriş yap
            login(request, user)
            return redirect("stepthree")
    return render(request, 'account/steptwo.html')


def stepthree(request):
    return render(request, 'account/stepthree.html')

def stepfour(request):
    return render(request, 'account/stepfour.html')

def stepfive(request):
    return render(request, 'account/stepfive.html')