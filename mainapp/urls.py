from django.urls import path
from .views import home_view, login_view, registration_view

urlpatterns = [
    path('', home_view, name='home'),
    path('sign-in/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
]