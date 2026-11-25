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
