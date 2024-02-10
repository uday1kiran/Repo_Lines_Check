# urls.py
from django.urls import path
from .views import download_and_analyze

urlpatterns = [
    path('', download_and_analyze, name='download_and_analyze'),
]
