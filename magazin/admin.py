from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Oluvchi, Sotuvchi, Mahsulot

def new_ism(modeladmin, request, queryset):
    queryset.update(ism="zorrobek")
def new_ism2(modeladmin, request, queryset):
    queryset.update(ism="qosimjon")

@admin.register(Oluvchi)
class OluvchiAdmin(ImportExportModelAdmin):
    list_display = ('ism', 'yosh', 'email')
    list_filter = ('ism', 'yosh', 'email')
    search_fields = ('ism', 'yosh', 'email')
    actions = (new_ism, new_ism2)

@admin.register(Sotuvchi)
class SotuvchiAdmin(admin.ModelAdmin):
    list_display = ('ism', 'familya', 'email', 'yosh')

@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    autocomplete_fields = ('oluvchi',)
    list_display = ('nom', 'rang', 'narh', 'oluvchi', 'sotuvchi')
