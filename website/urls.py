from django.urls import path
from .views import *

urlpatterns = [
    path('', WelcomeView.as_view(), name='home'),
    path('<slug:event>', EventInfoView.as_view(), name='event-info'),
    path('<slug:event>/register', AttendeeRegistrationView.as_view(), name='attendee-registration'),
]
