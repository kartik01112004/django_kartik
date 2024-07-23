from django.urls import path
from .views import viewIndex

urlpatterns = [
    
    path('index/', viewIndex),
]