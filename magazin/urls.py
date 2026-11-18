from django.template.defaulttags import url
from django.urls import path
from .views import HomeView
from ..config.urls import urlpatterns

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]