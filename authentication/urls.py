from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('validate-username',csrf_exempt(views.UsernameValidationView.as_view()), name='validate-username'),
    path('validate-email',csrf_exempt(views.EmailValidationView.as_view()), name='validate-email'),
    path('activate/<uidb64>/<token>',csrf_exempt(views.verificationView.as_view()), name='activate'),
]