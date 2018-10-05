from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect ,get_object_or_404
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *
from .models import *
from operator import itemgetter,attrgetter, methodcaller

def anasayfa(request):
    fakulteler=Fakulte.objects.all()
    akademisyenler=Akademisyen.objects.all()
    form=LoginForm(request.POST or None)
    if form.is_valid():
        kullanici_adi=request.POST.get('kullanici_adi')
        sifre=request.POST.get('sifre')
        kullanici=authenticate(username=kullanici_adi,password=sifre)
        if kullanici:
            login(request,kullanici)
            icerik={'fakulteler':fakulteler,'akademisyenler':akademisyenler,'kullanici':kullanici}
            return render(request,'mudek/anasayfa.html',icerik)
    icerik = {'fakulteler': fakulteler,'akademisyenler':akademisyenler,'form':form}
    return render(request,'mudek/anasayfa.html',icerik)

def cikis(request):
    logout(request)
    return redirect('/')

def cikis2(request):
    logout(request)
    return redirect('/ciktilar/')

def fakulteler(request,kullanici_id):
    fakulteler=Fakulte.objects.all()
    icerik={'fakulteler':fakulteler}
    return render(request,'mudek/fakulteler.html',icerik)

def fakulte_ekle(request,kullanici_id):
    fakulteler=Fakulte.objects.all()
    form=FakulteEkleForm(request.POST or None)
    if form.is_valid():
        fakulte_adi=request.POST.get('fakulte_adi')
        Fakulte.objects.create(fakulte_adi=fakulte_adi)
        return redirect('/{}/fakulteler'.format(kullanici_id))
    icerik={'fakulteler':fakulteler,'form':form}
    return render(request,'mudek/fakulte_ekle.html',icerik)

def fakulte_sil(request,kullanici_id,fakulte_id):
    Fakulte.objects.get(id=fakulte_id).delete()
    return redirect('/{}/fakulteler'.format(kullanici_id))

def bolumler(request,kullanici_id):
    fakulteler=Fakulte.objects.all()
    bolumler=Bolum.objects.all()
    icerik={'fakulteler':fakulteler,'bolumler':bolumler}
    return render(request,'mudek/bolumler.html',icerik)

def bolum_ekle(request,kullanici_id):
    fakulteler=Fakulte.objects.all()
    form=BolumEkleForm(request.POST or None)
    if form.is_valid():
        fakulte=Fakulte.objects.get(id=request.POST.get('fakulte'))
        bolum_adi=request.POST.get('bolum_adi')
        Bolum.objects.create(fakulte=fakulte,bolum_adi=bolum_adi)
        return redirect('/{}/bolumler'.format(kullanici_id))
    icerik={'fakulteler':fakulteler,'form':form}
    return render(request,'mudek/bolum_ekle.html',icerik)

def bolum_sil(request,kullanici_id,bolum_id):
    Bolum.objects.get(id=bolum_id).delete()
    return redirect('/{}/bolumler'.format(kullanici_id))

def akademisyenler(request,kullanici_id):
    fakulteler=Fakulte.objects.all()
    akademisyenler=Akademisyen.objects.all()
    icerik={'fakulteler':fakulteler,'akademisyenler':akademisyenler}
    return render(request,'mudek/akademisyenler.html',icerik)

def akademisyen_ekle(request,kullanici_id):
    fakulteler=Fakulte.objects.all()
    form=AkademisyenEkleForm(request.POST or None)
    if form.is_valid():
        bolum=Bolum.objects.get(id=request.POST.get('bolum'))
        aka_bilgi=request.POST.get('aka_bilgi')
        Akademisyen.objects.create(bolum=bolum,aka_bilgi=aka_bilgi)
        return redirect('/{}/akademisyenler'.format(kullanici_id))
    icerik={'fakulteler':fakulteler,'form':form}
    return render(request,'mudek/akademisyen_ekle.html',icerik)

def akademisyen_sil(request,kullanici_id,akademisyen_id):
    Akademisyen.objects.get(id=akademisyen_id).delete()
    return redirect('/{}/akademisyenler'.format(kullanici_id))

def ogrenciler(request,kullanici_id):
    fakulteler=Fakulte.objects.all()
    ogrenciler=Ogrenci.objects.all().order_by('ogr_no')
    icerik={'fakulteler':fakulteler,'ogrenciler':ogrenciler}
    return render(request,'mudek/ogrenciler.html',icerik)

def ogrenci_ekle(request,kullanici_id):
    fakulteler=Fakulte.objects.all()
    form=OgrenciEkleForm(request.POST or None)
    if form.is_valid():
        bolum=Bolum.objects.get(id=request.POST.get('bolum'))
        ogr_no=request.POST.get('ogr_no')
        ogr_ad=request.POST.get('ogr_ad')
        ogr_soyad=request.POST.get('ogr_soyad')
        Ogrenci.objects.create(bolum=bolum,ogr_no=ogr_no,ogr_ad=ogr_ad,ogr_soyad=ogr_soyad)
        return redirect('/{}/ogrenciler'.format(kullanici_id))
    icerik={'fakulteler':fakulteler,'form':form}
    return render(request,'mudek/ogrenci_ekle.html',icerik)

def ogrenci_sil(request,kullanici_id,ogrenci_id):
    Ogrenci.objects.get(id=ogrenci_id).delete()
    return redirect('/{}/ogrenciler'.format(kullanici_id))

def dersler(request,bolum_id,akademisyen_id): # akademisyenin dersleri listelenecek
    bolum=get_object_or_404(Bolum,id=bolum_id)
    fakulteler=Fakulte.objects.all()
    akademisyen=get_object_or_404(Akademisyen,id=akademisyen_id)
    akademisyenler=Akademisyen.objects.all()
    dersler = Ders.objects.filter(akademisyen__id = akademisyen_id)
    icerik = {'fakulteler': fakulteler,'dersler': dersler,'akademisyenler':akademisyenler,'akademisyen':akademisyen,'bolum':bolum}
    return render(request,'mudek/dersler.html',icerik)

def ders_ekle(request,bolum_id ,akademisyen_id):
    bolum = get_object_or_404(Bolum,id=bolum_id)
    ogrenciler=Ogrenci.objects.filter(bolum__id=bolum_id).all().order_by('ogr_no')
    ciktilar=Cikti.objects.filter(bolum__id=bolum_id).all().order_by('cikti_no')
    form = DersEkleForm(request.POST or None, ogrenciler=ogrenciler,ciktilar=ciktilar)
    if form.is_valid():
        bolum = get_object_or_404(Bolum,id=bolum_id)
        akademisyen = get_object_or_404(Akademisyen,id=akademisyen_id)
        ogrenciler = request.POST.getlist('ogrenci')
        ciktilar = request.POST.getlist('cikti')
        ders_kodu = request.POST.get('ders_kodu')
        ders_adi = request.POST.get('ders_adi')
        egit_yil = request.POST.get('egit_yil')
        egit_donem = request.POST.get('egit_donem')
        ders=Ders.objects.create(bolum=bolum,akademisyen=akademisyen,ders_kodu=ders_kodu,ders_adi=ders_adi,egit_yil=egit_yil,egit_donem=egit_donem)
        for i in ogrenciler:
            ders.ogrenci.add(i)
        for i in ciktilar:
            ders.cikti.add(i)
        return redirect('/{}/{}/'.format(bolum_id,akademisyen_id),bolum_id=bolum_id,akademisyen_id=akademisyen_id)
    icerik = {'form': form,'bolum':bolum}
    return render(request, "mudek/ders_ekle.html", icerik)


def sinavlar(request,bolum_id,akademisyen_id,ders_id):
    bolum= Bolum.objects.get(id=bolum_id)
    akademisyen = Akademisyen.objects.get(id = akademisyen_id)
    fakulteler=Fakulte.objects.all()
    akademisyenler=Akademisyen.objects.all()
    ders = Ders.objects.get(id = ders_id)
    sinavlar = Sinav.objects.filter(ders = ders_id).order_by('sinav_tarih')
    icerik = {'sinavlar':sinavlar,'fakulteler': fakulteler,'akademisyenler':akademisyenler,'bolum':bolum,'akademisyen':akademisyen,'ders':ders}
    return render(request,'mudek/sinavlar.html',icerik)

def sinav_ekle(request,bolum_id,akademisyen_id,ders_id):
    fakulteler=Fakulte.objects.all()
    akademisyenler=Akademisyen.objects.all()
    ders=get_object_or_404(Ders,id=ders_id)    
    form = SinavEkleForm(request.POST or None,ders=ders)
    if form.is_valid():
        ders = get_object_or_404(Ders,id=ders_id)
        tur = request.POST.get('sinav_tur')
        sinav_tarih = request.POST.get('sinav_tarih')
        Sinav.objects.create(ders=ders,sinav_tur=tur,sinav_tarih=sinav_tarih)
        return redirect('/{}/{}/{}/'.format(bolum_id,akademisyen_id,ders_id),bolum_id=bolum_id,akademisyen_id=akademisyen_id,ders_id=ders_id)

    icerik = {'fakulteler': fakulteler,'akademisyenler':akademisyenler,'form': form,'ders':ders}
    return render(request, 'mudek/sinav_ekle.html', icerik)
        
def sinav_sil(request,bolum_id,akademisyen_id,ders_id,sinav_id):
    Sinav.objects.get(id=sinav_id).delete()
    return HttpResponseRedirect('/{}/{}/{}/'.format(bolum_id,akademisyen_id,ders_id))

def sorular(request,bolum_id,akademisyen_id,ders_id,sinav_id):
    bolum = Bolum.objects.get(id=bolum_id)
    fakulteler=Fakulte.objects.all()
    akademisyen = Akademisyen.objects.get(id = akademisyen_id)
    akademisyenler=Akademisyen.objects.all()
    ders = Ders.objects.get(id = ders_id)
    sinav = Sinav.objects.get(id=sinav_id)
    sorular = Soru.objects.filter(sinav=sinav_id).order_by('soru_no')
    maxi=0
    for i in sorular:
        cikti_say=i.cikti.all().count()
        if maxi < cikti_say:
            maxi = cikti_say
    icerik = {'fakulteler': fakulteler,'akademisyenler':akademisyenler,'sorular':sorular,'maxi':maxi,'bolum':bolum,'akademisyen':akademisyen,'ders':ders,'sinav':sinav}
    return render(request,"mudek/sorular.html",icerik)

def soru_ekle(request,bolum_id,akademisyen_id,ders_id,sinav_id):
    bolum=Bolum.objects.get(id=bolum_id)
    fakulteler=Fakulte.objects.all()
    akademisyen = Akademisyen.objects.get(id = akademisyen_id)
    akademisyenler=Akademisyen.objects.all()
    sinav = Sinav.objects.get(id=sinav_id)
    ders = Ders.objects.get(id=ders_id)
    ciktilar = Ders.objects.get(id=ders_id).cikti.all().order_by('cikti_no')
    form = SoruEkleForm(request.POST or None,ciktilar=ciktilar,sinav=sinav)
    if form.is_valid():
        sinav = Sinav.objects.get(id=sinav_id)
        soru_no = request.POST.get('soru_no')
        soru_puan = request.POST.get('soru_puan')
        cikti = request.POST.getlist('cikti')
        soru=Soru.objects.create(sinav=sinav,soru_no=soru_no,soru_puan=soru_puan)
        cikti_dizi=[]
        for i in cikti:
            soru.cikti.add(i)
            cikti_dizi.append(Cikti.objects.get(bolum=bolum,id=i))
        for i in cikti_dizi:
            if i==ciktilar[0]:
                oranx=Soru_Cikti_Oran.objects.create(soru=soru,cikti=i,oran=request.POST.get('1'))
            elif i == ciktilar[1]:
                oranx=Soru_Cikti_Oran.objects.create(soru=soru,cikti=i,oran=request.POST.get('2'))
            elif i == ciktilar[2]:
                oranx=Soru_Cikti_Oran.objects.create(soru=soru,cikti=i,oran=request.POST.get('3'))
        return redirect('/{}/{}/{}/{}/'.format(bolum_id,akademisyen_id,ders_id,sinav_id),bolum_id=bolum_id,akademisyen_id=akademisyen_id,ders_id=ders_id,sinav_id=sinav_id)
    icerik ={'fakulteler': fakulteler,'akademisyenler':akademisyenler,'bolum':bolum,'akademisyen':akademisyen,'form':form,'ciktilar':ciktilar,'sinav':sinav,'ders':ders}
    return render(request,'mudek/soru_ekle.html',icerik)   

def soru_sil(request,bolum_id,akademisyen_id,ders_id,sinav_id,soru_id):
    delete=Soru.objects.get(id=soru_id).delete()
    return HttpResponseRedirect('/{}/{}/{}/{}/'.format(bolum_id,akademisyen_id,ders_id,sinav_id))

def ciktilar(request,fakulte_id):
    fakulte=Fakulte.objects.get(id=fakulte_id)
    fakulteler=Fakulte.objects.all()
    akademisyenler=Akademisyen.objects.all()
    ciktilar = Cikti.objects.extra(select={'ciktisira':'CAST(cikti_no AS INTEGER)'}).order_by('ciktisira')
    bolumler = Bolum.objects.filter(fakulte__id=fakulte_id)
    form=LoginForm(request.POST or None)
    if form.is_valid():
        kullanici_adi=request.POST.get('kullanici_adi')
        sifre=request.POST.get('sifre')
        kullanici=authenticate(username=kullanici_adi,password=sifre)
        if kullanici:
            login(request,kullanici)
            icerik={'ciktilar': ciktilar,'fakulteler':fakulteler,'fakulte':fakulte,'bolumler':bolumler,'kullanici':kullanici}
            return render(request,'mudek/ciktilar.html',icerik)
    icerik = {'akademisyenler':akademisyenler,'ciktilar': ciktilar,'fakulteler':fakulteler,'fakulte':fakulte,'bolumler':bolumler}
    return render(request,'mudek/ciktilar.html',icerik)

def cikti_ekle(request,bolum_id):
    bolum=Bolum.objects.get(id=bolum_id)
    fakulte_id=bolum.fakulte.id
    fakulteler=Fakulte.objects.all()
    akademisyenler=Akademisyen.objects.all()
    form = CiktiEkleForm(request.POST or None,bolum=bolum)
    if form.is_valid():
        bolum = Bolum.objects.get(id = bolum_id)
        cikti_no = request.POST.get('cikti_no')
        cikti_tani = request.POST.get('cikti_tani')
        cikti_tarih = request.POST.get('cikti_tarih')
        Cikti.objects.create(bolum=bolum,cikti_no=cikti_no,cikti_tani=cikti_tani,cikti_tarih=cikti_tarih)
        ciktilar=Cikti.objects.extra(select={'ciktisira':'CAST(cikti_no AS INTEGER)'}).order_by('ciktisira')
        return redirect('/ciktilar/{}/'.format(fakulte_id))
    icerik = {'bolum':bolum,'akademisyenler':akademisyenler,'fakulteler':fakulteler,'form': form}
    return render(request, "mudek/cikti_ekle.html", icerik)  

def cikti_sil(request,bolum_id,cikti_id):
    bolum=Bolum.objects.get(id=bolum_id)
    fakulte_id=bolum.fakulte.id
    Cikti.objects.get(bolum__id=bolum_id,id=cikti_id).delete()
    return redirect('/ciktilar/{}/'.format(fakulte_id))


def notlar(request,bolum_id,akademisyen_id,ders_id,sinav_id):
    bolum = Bolum.objects.get(id = bolum_id)
    fakulteler=Fakulte.objects.all()
    akademisyenler=Akademisyen.objects.all()
    akademisyen = Akademisyen.objects.get(id = akademisyen_id)
    ders = Ders.objects.get(id = ders_id)
    sinav = Sinav.objects.get(id = sinav_id)
    sorular = Soru.objects.filter(sinav = sinav_id).order_by('soru_no')
    soru_say=len(sorular)
    notlar=Notlar.objects.filter(soru__sinav=sinav_id).order_by('ogrenci__ogr_no')
    ogrenciler = Ders.objects.get(id=ders_id).ogrenci.all().order_by('ogr_no')
    ogrenciler2=[]
    for i in notlar:
        ogrenciler2.append(i.ogrenci)
    toplam=[]
    k=0
    for i in ogrenciler:
        topla=0
        for j in notlar:
            if j.ogrenci == i:
                topla+=j.al_not
        toplam.append([i,topla])
        k+=1
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

    icerik = {'notlar_dizi':notlar_dizi,'fakulteler': fakulteler,'akademisyenler':akademisyenler,'bolum':bolum, 'akademisyen':akademisyen, 'ders':ders,
                'sinav':sinav,'sorular':sorular, 'ogrenciler':ogrenciler,'ogrenciler2':ogrenciler2,'soru_say':soru_say,'notlar':notlar,'toplam':toplam}
    return render(request, 'mudek/notlar.html', icerik)

def notlandir(request,bolum_id,akademisyen_id,ders_id,sinav_id):
    bolum = Bolum.objects.get(id = bolum_id)
    fakulteler=Fakulte.objects.all()
    akademisyenler=Akademisyen.objects.all()
    akademisyen = Akademisyen.objects.get(id = akademisyen_id)
    ders = Ders.objects.get(id = ders_id)
    sinav = Sinav.objects.get(id = sinav_id)
    ogrenciler = Ders.objects.get(id=ders_id).ogrenci.all().order_by('ogr_no')
    sorular=Soru.objects.filter(sinav=sinav).order_by('soru_no')
    notlar2=Notlar.objects.filter(soru__sinav=sinav_id).order_by('ogrenci__ogr_no')
    soru_say=len(sorular)
    ogrenciler2=[]
    for i in notlar2:
        ogrenciler2.append(i.ogrenci)

    k = 1
    form_dizi=[]
    for i in ogrenciler:
        for j in sorular:
            form_dizi.append([[i,j,k]])
            k+=1

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
        for j in notlar2:
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
            for k in notlar2:
                if k.ogrenci == i[0][0] and k.soru == j[0]:
                    j.append(k)
                    break

    t=1
    for i in notlar_dizi:
        for j in i[0][1]:
            j.append(t)
            t+=1


    form=NotEkleForm(request.POST or None,ogrenciler=ogrenciler,ogrenciler2=ogrenciler2,sorular=sorular,notlar=notlar2)
    if form.is_valid():
        for i in notlar_dizi:
            for j in i[0][1]:
                if request.POST.get('{}'.format(j[2])):
                    if j[1]:
                        Notlar.objects.get(ogrenci=i[0][0],soru=j[0],al_not=j[1].al_not).delete()
                        Notlar.objects.create(ogrenci=i[0][0],soru=j[0],al_not=request.POST.get('{}'.format(j[2])))
                    else:
                        Notlar.objects.create(ogrenci=i[0][0],soru=j[0],al_not=request.POST.get('{}'.format(j[2])))
        notlar=Notlar.objects.extra(select={'notlar':'CAST(soru.soru_no AS INTEGER)'}).order_by('notlar')
        return redirect('/{}/{}/{}/{}/notlar/'.format(bolum_id,akademisyen_id,ders_id,sinav_id))
    icerik = {'fakulteler': fakulteler,'akademisyenler':akademisyenler,'form':form,'form_dizi':form_dizi,'bolum':bolum,'akademisyen':akademisyen,'ders':ders,'ogrenciler':ogrenciler,'sinav':sinav,'sorular':sorular,'soru_say':soru_say}
    return render(request,"mudek/not_ekle.html",icerik)
