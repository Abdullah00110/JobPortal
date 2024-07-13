from django.urls import path
from accounts.views import *
urlpatterns = [
    path('register/', Register.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('profile/', Profile.as_view(), name="profile"),
    path("change-password/", ChangePassword.as_view(), name="change-password"),
    path("password-reset-email/", PasswordResetEmail.as_view(), name="send-password-reset-email"),
    path("reset-password/<uid>/<token>", ResetPassword.as_view(), name="reset-password"),
    path("add-education/", AddEducation.as_view(), name="add-education"),
]
