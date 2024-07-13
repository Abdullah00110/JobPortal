from django.urls import path
from accounts.views import *
urlpatterns = [
    path('register/', Register.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('profile/', Profile.as_view(), name="profile"),
]
