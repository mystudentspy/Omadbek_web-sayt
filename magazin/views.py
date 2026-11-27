from django.shortcuts import render
from django.views import View
from .models import Mahsulot, Sotuvchi, Oluvchi


class HomeView(View):
    def get(self, request):
        return render(
            request,
            'home.html'
        )

class MahsulotView(View):
    def get(self, request):
        mahsulotlar = Mahsulot.objects.all()
        return render(
            request,
            'mahsulotlar/mahsulotlar.html',
            {
                "mahsulotlar": mahsulotlar,
            }
        )

class DetailMahsulotView(View):
    def get(self, request, pk):
        mahsulot = Mahsulot.objects.get(pk=pk)
        return render(
            request,
            'mahsulotlar/detail_mahsulot.html',
            {
                "mahsulot": mahsulot,
            }
        )

class SotuvchiView(View):
    def get(self, request):
        sotuvchilar = Sotuvchi.objects.all()
        return render(
            request,
            'sotuvchilar/sotuvchilar.html',
            {
                "sotuvchilar": sotuvchilar,
            }
        )

class DetailSotuvchiView(View):
    def get(self, request, pk):
        sotuvchi = Mahsulot.objects.get(pk=pk)
        return render(
            request,
            'sotuvchilar/detail_sotuvchi.html',
            {
                "sotuvchi": sotuvchi,
            }
        )

class OluvchiView(View):
    def get(self, request):
        oluvchilar = Oluvchi.objects.all()
        return render(
            request,
            'oluvchilar/oluvchilar.html',
            {
                "oluvchilar": oluvchilar,
            }
        )

class DetailOluvchiView(View):
    def get(self, request, pk):
        oluvchi = Mahsulot.objects.get(pk=pk)
        return render(
            request,
            'oluvchilar/detail_oluvchi.html',
            {
                "oluvchi": oluvchi,
            }
        )
