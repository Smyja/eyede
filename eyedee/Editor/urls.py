from django.urls import path
from Editor import views

urlpatterns = [
    path('', views.home, name='home'),
]
