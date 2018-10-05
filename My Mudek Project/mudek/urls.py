from django.conf.urls import url
from mudek.views import *

app_name = 'mudek'
urlpatterns = [
    url(r'^$', anasayfa, name='anasayfa'),
    url(r'^cikis/$', cikis, name='cikis'),    
    url(r'^(?P<bolum_id>[0-9]+)/(?P<akademisyen_id>[0-9]+)/$',dersler , name='dersler'),
    url(r'^(?P<bolum_id>[0-9]+)/(?P<akademisyen_id>[0-9]+)/ders_ekle/$',ders_ekle , name='ders_ekle'),
    url(r'^(?P<bolum_id>[0-9]+)/(?P<akademisyen_id>[0-9]+)/(?P<ders_id>[0-9]+)/$', sinavlar, name='sinavlar'),
    url(r'^(?P<bolum_id>[0-9]+)/(?P<akademisyen_id>[0-9]+)/(?P<ders_id>[0-9]+)/sinav_ekle/$', sinav_ekle, name='sinav_ekle'),
    url(r'^(?P<bolum_id>[0-9]+)/(?P<akademisyen_id>[0-9]+)/(?P<ders_id>[0-9]+)/(?P<sinav_id>[0-9]+)/sinav_sil/$', sinav_sil, name='sinav_sil'),
    url(r'^(?P<bolum_id>[0-9]+)/(?P<akademisyen_id>[0-9]+)/(?P<ders_id>[0-9]+)/(?P<sinav_id>[0-9]+)/$', sorular, name='sorular'),
    url(r'^(?P<bolum_id>[0-9]+)/(?P<akademisyen_id>[0-9]+)/(?P<ders_id>[0-9]+)/(?P<sinav_id>[0-9]+)/soru_ekle/$', soru_ekle, name='soru_ekle'),
    url(r'^(?P<bolum_id>[0-9]+)/(?P<akademisyen_id>[0-9]+)/(?P<ders_id>[0-9]+)/(?P<sinav_id>[0-9]+)/(?P<soru_id>[0-9]+)/soru_sil/$', soru_sil, name='soru_sil'),
    url(r'^(?P<bolum_id>[0-9]+)/(?P<akademisyen_id>[0-9]+)/(?P<ders_id>[0-9]+)/(?P<sinav_id>[0-9]+)/notlar/$', notlar, name='notlar'),
    url(r'^(?P<bolum_id>[0-9]+)/(?P<akademisyen_id>[0-9]+)/(?P<ders_id>[0-9]+)/(?P<sinav_id>[0-9]+)/notlandir/$', notlandir , name='notlandir'),
    url(r'^ciktilar/(?P<fakulte_id>[0-9]+)/$',ciktilar, name="ciktilar"),
    url(r'^ciktilar/(?P<bolum_id>[0-9]+)/cikti_ekle/$',cikti_ekle, name="cikti_ekle"),
    url(r'^ciktilar/(?P<bolum_id>[0-9]+)/(?P<cikti_id>[0-9]+)/cikti_sil/$',cikti_sil, name="cikti_sil"),
    url(r'^(?P<kullanici_id>[0-9]+)/fakulteler/$',fakulteler,name='fakulteler'),
    url(r'^(?P<kullanici_id>[0-9]+)/fakulte_ekle/$',fakulte_ekle,name='fakulte_ekle'),
    url(r'^(?P<kullanici_id>[0-9]+)/(?P<fakulte_id>[0-9]+)/fakulte_sil/$',fakulte_sil,name='fakulte_sil'),
    url(r'^(?P<kullanici_id>[0-9]+)/bolumler/$',bolumler,name='bolumler'),
    url(r'^(?P<kullanici_id>[0-9]+)/bolum_ekle/$',bolum_ekle,name='bolum_ekle'),
    url(r'^(?P<kullanici_id>[0-9]+)/(?P<bolum_id>[0-9]+)/bolum_sil/$',bolum_sil,name='bolum_sil'),
    url(r'^(?P<kullanici_id>[0-9]+)/akademisyenler/$',akademisyenler,name='akademisyenler'),
    url(r'^(?P<kullanici_id>[0-9]+)/akademisyen_ekle/$',akademisyen_ekle,name='akademisyen_ekle'),
    url(r'^(?P<kullanici_id>[0-9]+)/(?P<akademisyen_id>[0-9]+)/akademisyen_sil/$',akademisyen_sil,name='akademisyen_sil'),
    url(r'^(?P<kullanici_id>[0-9]+)/ogrenciler/$',ogrenciler,name='ogrenciler'),
    url(r'^(?P<kullanici_id>[0-9]+)/ogrenci_ekle/$',ogrenci_ekle,name='ogrenci_ekle'),
    url(r'^(?P<kullanici_id>[0-9]+)/(?P<ogrenci_id>[0-9]+)/ogrenci_sil/$',ogrenci_sil,name='ogrenci_sil'),
]