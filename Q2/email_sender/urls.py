from django.urls import path
from .views import sendEmail

urlpatterns = [
    path('send',sendEmail.as_view()),
]