from datetime import date
from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from operator import itemgetter,attrgetter, methodcaller

class LoginForm(forms.Form):
    kullanici_adi = forms.CharField()
    sifre = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        kullanici_adi = self.cleaned_data.get('kullanici_adi')
        sifre = self.cleaned_data.get('sifre')
        if kullanici_adi and sifre:
            kullanici = authenticate(username=kullanici_adi,password=sifre)
            if not kullanici:
                raise forms.ValidationError('Kullanıcı adını veya parolayı yanlış girdiniz!')
        return super(LoginForm,self).clean()

class FakulteEkleForm(forms.ModelForm):
    class Meta:
        model=Fakulte
        exclude=[]
    def __init__(self,*args,**kwargs):
        super(FakulteEkleForm, self).__init__(*args,**kwargs)
        self.fields['fakulte_adi']=forms.CharField()

class BolumEkleForm(forms.ModelForm):
    class Meta:
        model=Bolum
        fields=['fakulte','bolum_adi']
  #      exclude=[]
  #  def __init__(self,*args,**kwargs):
  #      super(BolumEkleForm,self).__init__(*args,**kwargs)
  #      self.fields['fakulte']=forms.ChoiceField()
  #      self.fields['bolum_adi']=forms.CharField()


class AkademisyenEkleForm(forms.ModelForm):

    class Meta:
        model=Akademisyen
        fields=['bolum','aka_bilgi']


class OgrenciEkleForm(forms.ModelForm):

    class Meta:
        model=Ogrenci
        fields=['bolum','ogr_no','ogr_ad','ogr_soyad']



class DersEkleForm(forms.ModelForm):
    
    class Meta:
        model = Ders
        exclude = ['bolum','akademisyen']

    def __init__(self, *args, **kwargs):
        ogrenciler = kwargs.pop('ogrenciler')
        ciktilar = kwargs.pop('ciktilar')
        super(DersEkleForm, self).__init__(*args,**kwargs)
        self.fields['ders_kodu'] = forms.CharField(max_length=15)
        self.fields['ders_adi'] = forms.CharField(max_length=50)
        #self.fields['ogrenci'].widget = forms.widgets.CheckboxSelectMultiple()
        #self.fields['ogrenci'].queryset = ogrenciler
        self.fields['cikti'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['cikti'].queryset = ciktilar
    
    def clean(self):
        cleaned_data=super(DersEkleForm,self).clean()
        ders_kodu=cleaned_data.get('ders_kodu')
        ders_adi=cleaned_data.get('ders_adi')
        egit_yil=cleaned_data.get('egit_yil')
        egit_donem=cleaned_data.get('egit_donem')
        for i in Ders.objects.all():
            if i.ders_kodu == ders_kodu and i.egit_yil == egit_yil and i.egit_donem == egit_donem:
                raise ValidationError({'ders_kodu':'Bu ders zaten kayıtlı'})
            elif i.ders_adi == ders_adi and i.egit_yil == egit_yil and i.egit_donem == egit_donem:
                raise ValidationError({'ders_adi':'Bu ders zaten kayıtlı'})
class SinavEkleForm(forms.ModelForm):
    

    class Meta:
        model = Sinav
        exclude = ['ders']

    def __init__(self,*args,**kwargs):
        gun=date.today().day
        ay=date.today().month
        yil=date.today().year
        ders=kwargs.pop('ders')
        super(SinavEkleForm, self).__init__(*args,**kwargs)
        if ay < 10 and gun < 10:
            self.fields['sinav_tarih'] = forms.DateField(initial='{}-0{}-0{}'.format(yil,ay,gun))
        elif ay < 10 and gun > 10:
            self.fields['sinav_tarih'] = forms.DateField(initial='{}-0{}-{}'.format(yil,ay,gun))
        elif ay > 12 and gun < 10:
            self.fields['sinav_tarih'] = forms.DateField(initial='{}-{}-0{}'.format(yil,ay,gun))
        self.ders=ders
    def clean(self):
        cleaned_data=super(SinavEkleForm,self).clean()
        sinav_tarih=cleaned_data.get('sinav_tarih')
        sinav_tur=cleaned_data.get('sinav_tur')
        for i in Sinav.objects.all():
            if i.ders == self.ders and i.sinav_tarih == sinav_tarih:
                raise ValidationError({'sinav_tur':'Bu tarihe kayıtlı bir sınav mevcut.'})
        #self.fields['sinav_tur'] = forms.ChoiceField()
        
class SoruEkleForm(forms.ModelForm):
    
    class Meta:
        model = Soru
        exclude = ['sinav']
    
    def __init__(self,*args,**kwargs):
        sinav=kwargs.pop('sinav')
        ciktilar = kwargs.pop('ciktilar')
        super(SoruEkleForm, self).__init__(*args, **kwargs)
        self.fields['soru_no'] = forms.IntegerField()
        self.fields['soru_puan'] = forms.IntegerField()
        self.fields['cikti'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['cikti'].queryset =ciktilar
        for i in range (1,len(ciktilar)+1):
            self.fields['{}'.format(i)] = forms.FloatField(required=False)
        self.sinav=sinav
    def clean(self):
        cleaned_data=super(SoruEkleForm,self).clean()
        soru_no=cleaned_data.get('soru_no')
        soru_puan=cleaned_data.get('soru_puan')
        if soru_no < 1:
            raise ValidationError({'soru_no':'En küçük değer 1 olabilir.'})
        elif soru_puan < 1 or soru_puan > 100:
            raise ValidationError({'soru_puan':'Lütfen 1-100 arasında bir değer giriniz.'})
        for i in Soru.objects.all():
            if i.soru_no == soru_no and i.sinav == self.sinav:
                raise ValidationError({'soru_no':'Bu soru zaten kayıtlı.'})
        
        
class CiktiEkleForm(forms.ModelForm):
    
    class Meta:
        model = Cikti
        exclude = ['bolum']

    def __init__(self,*args,**kwargs):
        gun=date.today().day
        ay=date.today().month
        yil=date.today().year
        bolum = kwargs.pop('bolum')
        super(CiktiEkleForm, self).__init__(*args,**kwargs)
        self.fields['cikti_no'] = forms.IntegerField(min_value=1)
        self.fields['cikti_tani'] = forms.CharField(widget=forms.Textarea())
        if ay < 10 and gun < 10:
            self.fields['cikti_tarih'] = forms.DateField(initial='{}-0{}-0{}'.format(yil,ay,gun))
        elif ay < 10 and gun > 10:
            self.fields['cikti_tarih'] = forms.DateField(initial='{}-0{}-{}'.format(yil,ay,gun))
        elif ay > 12 and gun < 10:
            self.fields['cikti_tarih'] = forms.DateField(initial='{}-{}-0{}'.format(yil,ay,gun))
        self.bolum = bolum
    def clean(self):
        cleaned_data=super(CiktiEkleForm,self).clean()
        cikti_no=cleaned_data.get('cikti_no') 
        for i in Cikti.objects.all():
            if i.cikti_no == cikti_no and i.bolum == self.bolum:
                raise ValidationError({'cikti_no':'Bu çıktı numarası sistemde kayıtlı'})


class NotEkleForm(forms.ModelForm):

    class Meta:
        model = Notlar
        exclude = ['soru','ogrenci','al_not']
        


    def __init__(self,*args,**kwargs):
        ogrenciler=kwargs.pop('ogrenciler')
        ogrenciler2=kwargs.pop('ogrenciler2')
        sorular=kwargs.pop('sorular')
        notlar=kwargs.pop('notlar')
        super(NotEkleForm,self).__init__(*args,**kwargs)
                

        x=0
        notlar_dizi=[]
        for i in ogrenciler:
            notlar_dizi.append([[i]])
            notlar_dizi[x][0].append([])
            for j in sorular:
                notlar_dizi[x][0][1].append([j])

            x+=1
        max_len=0
        for i in notlar_dizi:
           if len(i[0][1]) > max_len:
            max_len=len(i[0][1])

        for i in notlar_dizi:
            if len(i[0][1]) != max_len:
                for j in range(len(i[0][1]),max_len):
                    i[0][1].append([""])
                    
        
        for i in notlar_dizi:
            i.append([])
        for i in notlar_dizi:
            for j in notlar:
                if i[0][0] == j.ogrenci:
                    i[1].append(j.soru)


        for i in notlar_dizi:
            for j in i[0][1]:
                if j[0] not in sorular:
                    for k in sorular:
                        if k not in i[1]:
                            j[0]=k


        for i in notlar_dizi:
            k=0
            sirala=[]
            for j in i[0][1]:
                sirala.append(j[0])
            sirala.sort(key=attrgetter('soru_no'))  
            for j in sirala:
                i[0][1][k][0]=j
                k+=1
                
        for i in notlar_dizi:
            for j in i[0][1]:
                if j[0] not in i[1]:
                    j.append("")
                    continue
                for k in notlar:
                    if k.ogrenci == i[0][0] and k.soru == j[0]:
                        j.append(k)
                        break

        t=1
        for i in notlar_dizi:
            for j in i[0][1]:
                j.append(t)
                t+=1


        for i in notlar_dizi:
            for j in i[0][1]:
                if j[1]:
                    self.fields['{}'.format(j[2])]=forms.IntegerField(initial=j[1].al_not,required=False)
                else:
                    self.fields['{}'.format(j[2])]=forms.IntegerField(required=False)

