from django.contrib.auth import views as auth_views
from django.urls import path
from .import views

urlpatterns = [
    path("profile/", views.profile_request, name="profile"),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path("entry/", views.entry_request, name="entry"),
]
