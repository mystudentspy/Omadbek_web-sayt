from django.urls import path
from .views import (
    HomeView,
    MahsulotView, DetailMahsulotView,
    SotuvchiView, DetailSotuvchiView,
    OluvchiView,DetailOluvchiView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('mahsulotlar/', MahsulotView.as_view(), name='mahsulotlar'),
    path('mahsulotlar/<int:pk>/', DetailMahsulotView.as_view(), name='detail_mahsulot'),
    path('sotuvchilar/', SotuvchiView.as_view(), name='sotuvchilar'),
    path('sotuvchilar/<int:pk>/', DetailSotuvchiView.as_view(), name='detail_sotuvchi'),
    path('oluvchilar/', OluvchiView.as_view(), name='oluvchilar'),
    path('oluvchilar/<int:pk>/', DetailOluvchiView.as_view(), name='detail_oluvchi'),
]