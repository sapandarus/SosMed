from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("profile", views.profile, name="profile"),
    path("register", views.register_request, name='register'),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("search", views.search, name="search"),
    # path("follow", views.follow, name="follow"),
]