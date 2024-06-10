from doktor import Doktor
from hemşire import Hemşire
from personel import Personel
from hasta_sınıfı import Hasta
import pandas as pd

try:
    personel_1=Personel(1,"Ahmet","yılmaz","Muhasebe",20000)#nesneler oluşturuldu
    personel2=Personel(2,"Emin","Tetik","Reklam",17000)

    doktor1 = Doktor(3, "Zeynep", "Günesen", "Kardiyoloji", 500000, "Kardiyolog", 6, "Devlet Hastanesi")
    doktor2 = Doktor(4, "Mustafa", "pişkin", "Nöroloji", 65000, "Nörolog", 10, "Özel Hastane")
    doktor3 = Doktor(5, "Efe", "Alpaslan", "Pediatri", 100000, "Pediatrist", 8, "Üniversite Hastanesi")

    hemsire1 = Hemşire(6, "Kerem", "Tekin", "Cerrahi", 30000, 40, "Yoğun Bakım", "Devlet Hastanesi")
    hemsire2 = Hemşire(7, "Zübeyir", "Öztürk", "Dahiliye", 35000, 36, "Pediatri", "Özel Hastane")
    hemsire3 = Hemşire(8, "Hakan", "Koç", "Acil", 25000, 48, "Travma", "Üniversite Hastanesi")


    hasta1 = Hasta(1, "Ali", "Kaya", "1990-01-01", "Grip", "2023-06-01", "2023-06-10")
    hasta2 = Hasta(2, "Mehmet", "Yılmaz", "1985-05-15", "Kırık", "2023-06-05", "2023-06-20")
    hasta3 = Hasta(3, "Ayşe", "Demir", "1995-12-20", "Alerji", "2023-06-10", "2023-06-15")

    data=[
    {"No": personel_1.get_personel_no(), "Ad": personel_1.get_ad(), "Soyad": personel_1.get_soyad(), "Departman": personel_1.get_departman(), "Maaş": personel_1.get_maas()},
    {"No": personel2.get_personel_no(), "Ad": personel2.get_ad(), "Soyad": personel2.get_soyad(), "Departman": personel2.get_departman(), "Maaş": personel2.get_maas()},
    {"No": doktor1.get_personel_no(), "Ad": doktor1.get_ad(), "Soyad": doktor1.get_soyad(), "Departman": doktor1.get_departman(), "Maaş": doktor1.get_maas()},
    {"No": doktor2.get_personel_no(), "Ad": doktor2.get_ad(), "Soyad": doktor2.get_soyad(), "Departman": doktor2.get_departman(), "Maaş": doktor2.get_maas()},
    {"No": doktor3.get_personel_no(), "Ad": doktor3.get_ad(), "Soyad": doktor3.get_soyad(), "Departman": doktor3.get_departman(), "Maaş": doktor3.get_maas()},
    {"No": hemsire1.get_personel_no(), "Ad": hemsire1.get_ad(), "Soyad": hemsire1.get_soyad(), "Departman": hemsire1.get_departman(), "Maaş": hemsire1.get_maas()},
    {"No": hemsire2.get_personel_no(), "Ad": hemsire2.get_ad(), "Soyad": hemsire2.get_soyad(), "Departman": hemsire2.get_departman(), "Maaş": hemsire2.get_maas()},
    {"No": hemsire3.get_personel_no(), "Ad": hemsire3.get_ad(), "Soyad": hemsire3.get_soyad(), "Departman": hemsire3.get_departman(), "Maaş": hemsire3.get_maas()},
    ]



    data_frame=pd.DataFrame(data)#çalışan bilgileri yazdırılıyor
    print(data_frame.to_string())

    doktor_list = [doktor1, doktor2, doktor3]
    uzmanlıklar={}#uzman doktor sözlüğü oluşturuluyor.
    for doktor in doktor_list:
        uzmanlık=doktor.get_uzmanlık()
        if uzmanlık in uzmanlıklar:
            uzmanlıklar[uzmanlık]+=1
        else:
            uzmanlıklar[uzmanlık] = 1

    for uzmanlık, sayı in uzmanlıklar.items():
        print(f"{uzmanlık}: {sayı}")

    deneyimli_doktor=0
    for doktor in doktor_list:
        if doktor._deneyim_yılı>5:
            deneyimli_doktor+=1
    print(f"Deneyimli doktor sayısı: {deneyimli_doktor}")

    hasta_list = [
        {"No": hasta1.get_hasta_no(), "Ad": hasta1.get_ad(), "Soyad": hasta1.get_soyad(),
         "Doğum Tarihi": hasta1.get_dogum_tarihi(), "Hastalık": hasta1.get_hastalik(),
         "Tedavi Süresi (gün)": hasta1.tedavi_sure()},
        {"No": hasta2.get_hasta_no(), "Ad": hasta2.get_ad(), "Soyad": hasta2.get_soyad(),
         "Doğum Tarihi": hasta2.get_dogum_tarihi(), "Hastalık": hasta2.get_hastalik(),
         "Tedavi Süresi (gün)": hasta2.tedavi_sure()},
        {"No": hasta3.get_hasta_no(), "Ad": hasta3.get_ad(), "Soyad": hasta3.get_soyad(),
         "Doğum Tarihi": hasta3.get_dogum_tarihi(), "Hastalık": hasta3.get_hastalik(),
         "Tedavi Süresi (gün)": hasta3.tedavi_sure()}
    ]

    hasta=pd.DataFrame(hasta_list)
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")

    df_hasta_sorted = hasta.sort_values(by="Ad")# hastaların ismi alfabetik sıraya göre dizilme
    print("\nAlfabetik sıraya göre sıralanmış Hasta DataFrame:")
    print(df_hasta_sorted)

    print("-------------------------------------------------------")
    print("-------------------------------------------------------")

    yuksek_maas_personel = data_frame[data_frame["Maaş"]> 7000]#maası 7000 lira üzeri olan çalışan listesi
    print("\nMaaşı 7000 liranın üzerinde olan personeller:")
    print(yuksek_maas_personel)


except Exception as e:
    print(f"Hata oluştu: {e}")