from django.urls import path
from .views import start_crawler

urlpatterns = [
    path('start-crawler/', start_crawler, name='start-crawler'),
]