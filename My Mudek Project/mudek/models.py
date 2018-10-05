from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator,MinValueValidator


"""
BOLUM=(('B_M','Bilgisayar Mühendisliği'),('EE_M','Elektrik Elektronik Mühendisliği'),
		   ('H_M','Harita Mühendisliği'),('I_M','İnşaat Mühendisliği'),
		   ('JF_M','Jeofizik Mühendisliği'),('J_M','Jeoloji Mühendisliği'),
		   ('MD_M','Maden Mühendisliği'),('MK_M','Makine Mühendisliği'),('MVM_M','Metalurji ve Malzeme Mühendisliği'))

BOLUM2=(('O_M','Orman Mühendisliği'),('OE_M','Orman Endüstri Mühendisliği'))

Ciktilar=
1.   Matematik, fen bilimleri ve kendi dalları ile ilgili mühendislik konularında yeterli bilgi birikimi; bu alanlardaki kuramsal ve uygulamalı bilgileri mühendislik problemlerini modelleme ve çözme için uygulayabilme becerisi.

2.   Karmaşık mühendislik problemlerini saptama, tanımlama, formüle etme ve çözme becerisi; bu amaçla uygun analiz ve modelleme yöntemlerini seçme ve uygulama becerisi.

3.   Karmaşık bir sistemi, süreci, cihazı veya ürünü gerçekçi kısıtlar ve koşullar altında, belirli gereksinimleri karşılayacak şekilde tasarlama becerisi; bu amaçla modern tasarım yöntemlerini uygulama becerisi.

4.   Mühendislik uygulamaları için gerekli olan modern teknik ve araçları geliştirme, seçme ve kullanma becerisi; bilişim teknolojilerini etkin bir şekilde kullanma becerisi.

5.   Mühendislik problemlerinin incelenmesi için deney tasarlama, deney yapma, veri toplama, sonuçları analiz etme ve yorumlama becerisi.

6.   Disiplin içi ve çok disiplinli takımlarda etkin biçimde çalışabilme becerisi; bireysel çalışma becerisi.

7.   Türkçe sözlü ve yazılı etkin iletişim kurma becerisi; en az bir yabancı dil bilgisi.

8.   Yaşam boyu öğrenmenin gerekliliği bilinci; bilgiye erişebilme, bilim ve teknolojideki gelişmeleri izleme ve kendini sürekli yenileme becerisi.

9.   Mesleki ve etik sorumluluk bilinci.

10.   Proje yönetimi ile risk yönetimi ve değişiklik yönetimi gibi iş hayatındaki uygulamalar hakkında bilgi; girişimcilik, yenilikçilik ve sürdürebilir kalkınma hakkında farkındalık.

11.   Mühendislik uygulamalarının evrensel ve toplumsal boyutlarda sağlık, çevre ve güvenlik üzerindeki etkileri ile çağın sorunları hakkında bilgi; mühendislik çözümlerinin hukuksal sonuçları konusunda farkındalık. 

12.   Karmaşık donanımların, yazılımların ve bunları içeren sistemlerin tasarım ve analizi için gerekli olasılık ve istatistik bilgisi, türev, integral ve ayrık matematik hesapları da içerecek biçimde matematik bilgisi, temel bilimler, bilgisayar ve mühendislik bilimleri konularında bilgi.





"""

BOLUMLER=(('Bilgisayar Mühendisliği','Bilgisayar Mühendisliği'),('Elektrik Elektronik Mühendisliği','Elektrik Elektronik Mühendisliği'),
		   ('Harita Mühendisliği','Harita Mühendisliği'),('İnşaat Mühendisliği','İnşaat Mühendisliği'),
		   ('Jeofizik Mühendisliği','Jeofizik Mühendisliği'),('Jeoloji Mühendisliği','Jeoloji Mühendisliği'),
		   ('Maden Mühendisliği','Maden Mühendisliği'),('Makine Mühendisliği','Makine Mühendisliği'),('Metalurji ve Malzeme Mühendisliği','Metalurji ve Malzeme Mühendisliği'),
		   ('Orman Mühendisliği','Orman Mühendisliği'),('Orman Endüstri Mühendisliği','Orman Endüstri Mühendisliği')
	)

yil=date.today().year
d=[]
data=[]
u=0
for i in range(2000,yil+1):
	d.append('{} - {} , {} - {}'.format(str(i),str(i+1),str(i),str(i+1)))
	data.append(tuple(d[u].split(",")))
	u+=1


EGIT_YIL=tuple(data)

DONEM=(('GÜZ','GÜZ'),('BAHAR','BAHAR'))

SINAV_TUR=(('Ara Sınav','Ara Sınav'),('Final','Final'),
		   ('Uygulama','Uygulama'),('Bütünleme','Bütünleme'),('Mezuniyet','Mezuniyet'))


class Fakulte(models.Model):

	fakulte_adi=models.CharField(max_length=25,verbose_name="Fakülte Adı")
	
	class Meta:
		verbose_name="Fakülteler"
		verbose_name_plural="Fakülteler"

	def __str__(self):
		return self.fakulte_adi
	def clean(self):
		for i in Fakulte.objects.filter(fakulte_adi=self.fakulte_adi):
			if i.fakulte_adi==self.fakulte_adi:
				raise ValidationError({'fakulte_adi':'Sistemde Kayıtlı.'})
class Bolum(models.Model):
	
	fakulte=models.ForeignKey(Fakulte,on_delete=models.CASCADE)
	bolum_adi=models.CharField(verbose_name="Bölüm Adı",max_length=50,choices=BOLUMLER,default="Bilgisayar Mühendisliği")
	
	class Meta:
		verbose_name="Bölümler"
		verbose_name_plural="Bölümler"

	def __str__(self):
		return '{}'.format(self.bolum_adi)
"""	
	def clean(self):
		temp=Bolum.objects.all()
		for i in temp:
			if i.bolum_adi == self.bolum_adi:
				raise ValidationError({'bolum_adi':'Sistemde Kayıtlı.'})
			elif self.fakulte.fakulte_adi == 'Mühendislik Fakültesi' and self.bolum_adi == 'Orman Mühendisliği':
				raise ValidationError({'bolum_adi':'Fakülte Uyuşmazlığı.'})
			elif self.fakulte.fakulte_adi == 'Mühendislik Fakültesi' and self.bolum_adi == 'Orman Endüstri Mühendisliği':
				raise ValidationError({'bolum_adi':'Fakülte Uyuşmazlığı.'})
			elif self.fakulte.fakulte_adi == 'Orman Fakültesi' and self.bolum_adi == 'Bilgisayar Mühendisliği':
				raise ValidationError({'bolum_adi':'Fakülte Uyuşmazlığı.'})
			elif self.fakulte.fakulte_adi == 'Orman Fakültesi' and self.bolum_adi == 'Elektrik Elektronik Mühendisliği':
				raise ValidationError({'bolum_adi':'Fakülte Uyuşmazlığı.'})
			elif self.fakulte.fakulte_adi == 'Orman Fakültesi' and self.bolum_adi == 'Harita Mühendisliği':
				raise ValidationError({'bolum_adi':'Fakülte Uyuşmazlığı.'})
			elif self.fakulte.fakulte_adi == 'Orman Fakültesi' and self.bolum_adi == 'İnşaat Mühendisliği':
				raise ValidationError({'bolum_adi':'Fakülte Uyuşmazlığı.'})
			elif self.fakulte.fakulte_adi == 'Orman Fakültesi' and self.bolum_adi == 'Jeofizik Mühendisliği':
				raise ValidationError({'bolum_adi':'Fakülte Uyuşmazlığı.'})
			elif self.fakulte.fakulte_adi == 'Orman Fakültesi' and self.bolum_adi == 'Jeoloji Mühendisliği':
				raise ValidationError({'bolum_adi':'Fakülte Uyuşmazlığı.'})
			elif self.fakulte.fakulte_adi == 'Orman Fakültesi' and self.bolum_adi == 'Maden Mühendisliği':
				raise ValidationError({'bolum_adi':'Fakülte Uyuşmazlığı.'})
			elif self.fakulte.fakulte_adi == 'Orman Fakültesi' and self.bolum_adi == 'Makine Mühendisliği':
				raise ValidationError({'bolum_adi':'Fakülte Uyuşmazlığı.'})
			elif self.fakulte.fakulte_adi == 'Orman Fakültesi' and self.bolum_adi == 'Metalurji ve Malzeme Mühendisliği':
				raise ValidationError({'bolum_adi':'Fakülte Uyuşmazlığı.'})
	
"""

	#def save(self,*args, **kwargs):
	#	self.full_clean()
	#	super().save(*args,**kwargs)
"""
	if(fakulte.fakulte_adi=="Mühendislik Fakültesi"):
		bolum_adi=models.CharField(verbose_name="Bölüm Adı",max_length=50,choices=BOLUM,default="Bilgisayar Mühendisliği")
		def __str__(self):
			return '{} - {}'.format(self.fakulte.fakulte_adi,self.bolum_adi)
	if(fakulte.fakulte_adi=="Orman Fakültesi"): 
		bolum_adi=models.CharField(verbose_name="Bolum Adi",max_length=50,choices=BOLUM2,default="Orman Mühendisliği")
		def __str__(self):
			return '{} - {}'.format(self.fakulte.fakulte_adi,self.bolum_adi)
			"""



class Akademisyen(models.Model):
	bolum=models.ForeignKey(Bolum,on_delete=models.CASCADE)
	aka_bilgi=models.CharField(verbose_name="Akademisyen Ad-Soyad",max_length=60)
	class Meta:
		verbose_name="Akademisyenler"
		verbose_name_plural="Akademisyenler"
	def __str__(self):
		return '{} - {}'.format(self.bolum.bolum_adi,self.aka_bilgi)

class Cikti(models.Model):
	bolum=models.ForeignKey(Bolum,on_delete=models.CASCADE)
	cikti_no=models.PositiveIntegerField(verbose_name="Çıktı Numarası",validators=[MinValueValidator(1),MaxValueValidator(20)])
	cikti_tani=models.TextField(verbose_name="Çıktı Tanımı")
	cikti_tarih=models.DateField(verbose_name="Çıktı Tarihi")
	class Meta:
		verbose_name="Çıktılar"
		verbose_name_plural="Çıktılar"
	def __str__(self):
		return 'Çıktı No({}) - {}'.format(self.cikti_no,self.bolum.bolum_adi)
"""
	def clean(self):
		temp=Cikti.objects.all()
		for i in temp:
			if i.cikti_no==self.cikti_no and i.bolum==self.bolum:
				raise ValidationError({'cikti_no':'Sistemde Kayıtlı.'})

"""
class Ogrenci(models.Model):
	bolum=models.ForeignKey(Bolum,on_delete=models.CASCADE)
	ogr_no=models.PositiveIntegerField(verbose_name="Öğrenci No",validators=[MinValueValidator(1)])
	ogr_ad=models.CharField(verbose_name="Öğrenci Ad",max_length=35)
	ogr_soyad=models.CharField(verbose_name="Öğrenci Soyad",max_length=25)
	class Meta:
		verbose_name="Öğrenciler"
		verbose_name_plural="Öğrenciler"
	def __str__(self):
		return '{} - {} - {} - {}'.format(self.bolum.bolum_adi,self.ogr_no,self.ogr_ad,self.ogr_soyad)
"""	
	def clean(self):
		temp=Ogrenci.objects.all()
		for i in temp:
			if i.ogr_no==self.ogr_no:
				raise ValidationError({'ogr_no':'Sistemde Kayıtlı.'})
"""

class Ders(models.Model):
	bolum=models.ForeignKey(Bolum,on_delete=models.CASCADE)
	akademisyen=models.ForeignKey(Akademisyen,on_delete=models.CASCADE)
	ogrenci=models.ManyToManyField(Ogrenci)
	cikti=models.ManyToManyField(Cikti)
	ders_kodu=models.CharField(verbose_name="Ders Kodu",max_length=15)
	ders_adi=models.CharField(verbose_name="Ders Adı",max_length=50)
	egit_yil=models.CharField(verbose_name="Eğitim Yılı",max_length=13,choices=EGIT_YIL)
	egit_donem=models.CharField(verbose_name="Dönem",max_length=10,choices=DONEM)
	class Meta:
		verbose_name="Dersler"
		verbose_name_plural="Dersler"
	def __str__(self):
		return '{} - {} - {}'.format(self.ders_kodu,self.akademisyen.aka_bilgi,self.bolum.bolum_adi)
"""

	def clean(self):
		temp=Ders.objects.all()
		for i in temp:
			if i.ders_kodu==self.ders_kodu and i.egit_yil==self.egit_yil and i.egit_donem==self.egit_donem:
				raise ValidationError({'ders_kodu':'Sistemde Kayıtlı.'})
			elif i.ders_adi==self.ders_adi and i.egit_yil==self.egit_yil and i.egit_donem==self.egit_donem:
				raise ValidationError({'ders_adi':'Sistemde Kayıtlı.'})
		if self.bolum != self.akademisyen.bolum:
			raise ValidationError({'akademisyen':'Hatalı Seçim.'})
		
		#temp=Ders.objects.filter(ders_kodu=self.ders_kodu,egit_yil=self.egit_yil,egit_donem=self.egit_donem)
		#temp2=Ders.objects.filter(ders_adi=self.ders_adi,egit_yil=self.egit_yil,egit_donem=self.egit_donem)
		#for i in temp:
		#	if i.ders_kodu==self.ders_kodu and i.egit_yil==self.egit_yil and i.egit_donem==self.egit_donem:
		#		raise ValidationError({'ders_kodu':'Sistemde Kayıtlı.'})
		#for j in temp2:
		#	if j.ders_adi==self.ders_adi and j.egit_yil==self.egit_yil and j.egit_donem==self.egit_donem:
		#		raise ValidationError({'ders_adi':'Sistemde Kayıtlı.'})
		#if self.bolum!=self.akademisyen.bolum:
		#	raise ValidationError({'akademisyen':'Hatalı Seçim.'})
"""


class Sinav(models.Model):
	ders=models.ForeignKey(Ders,on_delete=models.CASCADE)
	sinav_tur=models.CharField(verbose_name="Sınav Türü",max_length=25,choices=SINAV_TUR)
	sinav_tarih=models.DateField(verbose_name="Sınav Tarihi")
	class Meta:
		verbose_name="Sınavlar"
		verbose_name_plural="Sınavlar"
	def __str__(self):
		return '{} - {} - {} - {}'.format(self.ders.bolum.bolum_adi,self.ders.ders_kodu,self.sinav_tur,self.sinav_tarih)

"""

	def clean(self):
		temp=Sinav.objects.all()
		for i in temp:
			if i.ders==self.ders and i.sinav_tarih==self.sinav_tarih:
				raise ValidationError({'sinav_tarih':'Sistemde Kayıtlı.'})
			elif (i.ders ==self.ders and i.sinav_tur=='Mezuniyet' and self.sinav_tur=='Mezuniyet') or (i.ders==self.ders and i.sinav_tur=='Final' and self.sinav_tur=='Final') or (i.ders == self.ders and i.sinav_tur=='Bütünleme' and self.sinav_tur=='Bütünleme'):
				raise ValidationError({'sinav_tur':'Sistemde Kayıtlı.'})

"""

class Soru(models.Model):
	sinav=models.ForeignKey(Sinav,on_delete=models.CASCADE)
	soru_no=models.PositiveIntegerField(verbose_name="Soru Numarası")
	soru_puan=models.PositiveIntegerField(verbose_name="Soru Puanı")
	cikti=models.ManyToManyField(Cikti)
	class Meta:
		verbose_name="Sorular"
		verbose_name_plural="Sorular"
	def __str__(self):
		return '{} - {} - {}({}) - {}.Soru({})'.format(self.sinav.ders.bolum.bolum_adi,self.sinav.ders.ders_kodu,self.sinav.sinav_tur,self.sinav.sinav_tarih,self.soru_no,self.soru_puan)

class Soru_Cikti_Oran(models.Model):
	soru=models.ForeignKey(Soru,on_delete=models.CASCADE)
	cikti=models.ForeignKey(Cikti,on_delete=models.CASCADE)
	oran=models.FloatField(verbose_name="Soru Çıktı Oranı")
	
	class Meta:
		verbose_name="Soru Çıktı Oranları"
		verbose_name_plural="Soru Çıktı Oranları"
	def __str__(self):
		return'{} - {} - {}'.format(self.soru,self.cikti,self.oran)


class Notlar(models.Model):
	soru=models.ForeignKey(Soru,on_delete=models.CASCADE)
	ogrenci=models.ForeignKey(Ogrenci,on_delete=models.CASCADE)
	al_not=models.PositiveIntegerField(verbose_name="Alınan Not",validators=[MinValueValidator(1)])
	class Meta:
		verbose_name="Notlar"
		verbose_name_plural="Notlar"
	def __str__(self):
		return '{} - {} - {}'.format(self.ogrenci.ogr_no,self.soru.soru_no,self.al_not)
	"""def clean(self):
		temp=Notlar.objects.all()
		for i in temp:
			if i.soru==self.soru and i.ogrenci==self.ogrenci:
				raise ValidationError({'ogrenci':'Sistemde Kayıtlı.'})
		if self.soru.sinav.ders.bolum!=self.ogrenci.bolum:
			raise ValidationError({'ogrenci':'Öğrenci Başka Bölüme Kayıtlı.'})
		
		if self.soru.soru_puan < self.al_not:
			raise ValidationError({'al_not':'Geçersiz Notlama(Max:{})'.format(self.soru.soru_puan)})
"""
class Cikti_Basari(models.Model):
	cikti=models.ForeignKey(Cikti,on_delete=models.CASCADE)
	basari_oran=models.FloatField(verbose_name="Çıktı Başarı Oranı",validators=[MaxValueValidator(100)])
	class Meta:
		verbose_name="Çıktı Başarı Oranı"
		verbose_name_plural="Çıktı Başarı Oranı"
	def __str__(self):
		return '{} - {}'.format(self.soru.soru_no,self.basari_oran)

class Ogr_Cikti_Bas(models.Model):
	ogrenci=models.ForeignKey(Ogrenci,on_delete=models.CASCADE)
	cikti=models.ForeignKey(Cikti,on_delete=models.CASCADE)
	ogr_cikti_bas=models.FloatField(verbose_name="Öğrenci Çıktı Başarı Oranı")
	class Meta:
		verbose_name="Öğrenci Çıktı Başarı Oranı"
		verbose_name_plural="Öğrenci Çıktı Başarı Oranı"
	def __str__(self):
		return '{} - {} - {}'.format(self.ogrenci.ogr_no,self.cikti.cikti_no,self.cikti_basari_oran)
"""
	def clean(self):
		temp=Ogr_Cikti_Bas.objects.all()
		for i in temp:
			if i.ogrenci==self.ogrenci and i.cikti==self.cikti:
				raise ValidationError({'cikti':'Sistemde Kayıtlı.'})
		if self.ogrenci.bolum!=self.cikti.bolum:
			raise ValidationError({'cikti':'Hatalı Seçim.'})
"""