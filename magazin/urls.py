from django.urls import path
from .views import (
    HomeView,
    MahsulotView,
    SotuvchiView,
    OluvchiView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('mahsulotlar/', MahsulotView.as_view(), name='mahsulotlar'),
    path('sotuvchilar/', SotuvchiView.as_view(), name='sotuvchilar'),
    path('oluvchilar/', OluvchiView.as_view(), name='oluvchilar'),
]