from django.urls import path
from .import views

# http://127.0.0.1:8000/            => homepage
# http://127.0.0.1:8000/index       => homepage
# http://127.0.0.1:8000/login       => login
# http://127.0.0.1:8000/signup      => signup
# http://127.0.0.1:8000/lates/1     => latest

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index),
    path("signup", views.signup, name="signup"),
    path("latest", views.latest, name="latest"),
    path("latest/<int:id>", views.latest_details, name="latest_details"),

]
