from django.contrib import admin
from .models import *


@admin.register(Fakulte)
class FakulteAdmin(admin.ModelAdmin):
	list_display=['fakulte_adi']
	list_display_links=['fakulte_adi']
	search_fields=['fakulte_adi']

@admin.register(Bolum)
class BolumAdmin(admin.ModelAdmin):
	list_display=['bolum_adi','fakulte']
	list_display_links=['fakulte','bolum_adi']
	search_fields=['fakulte','bolum_adi']
	list_filter=['fakulte']


@admin.register(Akademisyen)
class AkademisyenAdmin(admin.ModelAdmin):
	list_display=['aka_bilgi','bolum']
	search_fields=['bolum','aka_bilgi']
	list_display_links=['bolum','aka_bilgi']
	list_filter=['bolum']

@admin.register(Ogrenci)
class OgrenciAdmin(admin.ModelAdmin):
	list_display=['ogr_no','ogr_ad','ogr_soyad','bolum']
	list_display_links=['bolum','ogr_no','ogr_ad','ogr_soyad']
	search_fields=['bolum','ogr_no','ogr_ad','ogr_soyad']
	list_filter=['bolum']

@admin.register(Cikti)
class CiktiAdmin(admin.ModelAdmin):
	list_display=['cikti_no','bolum']
	list_display_links=['cikti_no','bolum']
	search_fields=['cikti_no','bolum']
	list_filter=['bolum']

@admin.register(Ders)
class DersAdmin(admin.ModelAdmin):
	list_display=['ders_kodu','ders_adi','egit_donem','egit_yil','bolum']
	list_display_links=['ders_kodu','ders_adi','egit_yil','egit_donem','bolum']
	search_fields=['ders_kodu','ders_adi','egit_yil','egit_donem','bolum']
	list_filter=['bolum','egit_donem']

@admin.register(Sinav)
class SinavAdmin(admin.ModelAdmin):
	list_display=['ders','sinav_tur','sinav_tarih']
	list_display_links=['sinav_tur','ders','sinav_tarih']
	search_fields=['sinav_tur','ders','sinav_tarih']
	list_filter=['ders','sinav_tarih']

@admin.register(Soru)
class SoruAdmin(admin.ModelAdmin):
	list_display=['sinav','soru_no','soru_puan']
	list_display_links=['soru_no','soru_puan','sinav']
	search_fields=['soru_no','soru_puan','sinav']
	list_filter=['sinav']

@admin.register(Soru_Cikti_Oran)
class S_C_Admin(admin.ModelAdmin):
	list_display=['soru','cikti','oran']
	list_display_links=['soru','cikti','oran']
	search_fields=['cikti','soru']
	list_filter=['cikti']

@admin.register(Notlar)
class NotAdmin(admin.ModelAdmin):
	list_display=['ogrenci','soru','al_not']
	list_display_links=['ogrenci','soru','al_not']
	search_fields=['ogrenci','soru','al_not']
	list_filter=['soru','ogrenci']

@admin.register(Cikti_Basari)
class C_B_Admin(admin.ModelAdmin):
	list_display=['cikti','basari_oran']
	list_display_links=['cikti','basari_oran']
	search_fields=['cikti','basari_oran']
	list_filter=['cikti']

@admin.register(Ogr_Cikti_Bas)
class OgrCiktiBasAdmin(admin.ModelAdmin):
	list_display=['ogrenci','cikti','ogr_cikti_bas']
	list_display_links=['ogrenci','cikti','ogr_cikti_bas']
	search_fields=['ogrenci','cikti','ogr_cikti_bas']
	list_filter=['cikti']