from .views import *
from django.urls import path


urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('about/', about)
]
