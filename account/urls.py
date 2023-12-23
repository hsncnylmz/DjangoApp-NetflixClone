from django.contrib.auth import views as auth_views
from django.urls import path
from .import views

urlpatterns = [
    path("login", views.login_request, name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout'), name='logout'),
    path('stepone/', views.stepone, name='stepone'),
    path('steptwo/', views.steptwo_request, name='steptwo'),
    path('stepthree/', views.stepthree, name='stepthree'),
    path('stepfour/', views.stepfour, name='stepfour'),
    path('stepfive/', views.stepfive, name='stepfive'),
]
