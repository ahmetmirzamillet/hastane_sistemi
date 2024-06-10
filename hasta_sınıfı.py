from _datetime import datetime # datetime kütüphanesi eklendi

class Hasta: #hasta sınıfı eklenip hastanın bilgileri kaydediliyor.
    def __init__(self,hasta_no,ad,soyad,doğum_tarihi,hastalık,tedavi_baslangic,tedavi_bitis):
        self._hasta_no = hasta_no
        self._ad = ad
        self._soyad =soyad
        self._doğum_tarihi=doğum_tarihi
        self._hastalık=hastalık
        self._tedavi_baslangic=tedavi_baslangic
        self._tedavi_bitis=tedavi_bitis

    def tedavi_sure(self):# tedavi suresi metodu eklenip hastanın tedavi süresini hesaplayan metod.
        baslangic = datetime.strptime(self._tedavi_baslangic, '%Y-%M-%d')
        bitis = datetime.strptime(self._tedavi_bitis, '%Y-%M-%d')
        sure = bitis - baslangic
        return sure.days

    def get_hasta_no(self):
        return self._hasta_no
    def set_hasta_no(self,hasta_no):
        self._hasta_no = hasta_no

    def get_ad(self):
        return self._ad
    def set_ad(self, ad):
        self._ad = ad

    def get_soyad(self):
        return self._soyad
    def set_soyad(self, soyad):
        self._soyad = soyad

    def get_dogum_tarihi(self):
        return self._doğum_tarihi
    def set_doğum_tarihi(self,doğum_tarihi):
        self._doğum_tarihi=doğum_tarihi

    def get_hastalik(self):
        return self._hastalık
    def set_hastalık(self,hastalık):
        self._hastalık=hastalık


    def get_tedavi_sure(self):
        return self._tedavi_baslangic

    def set_tedavi_sure(self, tedavi_baslangic):
        self._tedavi_baslangic = tedavi_baslangic

    def get_tedavi_bitis(self):
        return self._tedavi_bitis

    def set_tedavi_bitis(self, tedavi_bitis):
        self._tedavi_bitis = tedavi_bitis


    def __str__(self):
        return (f"Hasta No: {self._hasta_no}, Ad: {self._ad}, Soyad: {self._soyad}, "
                f"Doğum Tarihi: {self._doğum_tarihi}, Hastalık: {self._hastalık}, "
                f"Tedavi Başlangıç: {self._tedavi_baslangic}, Tedavi Bitiş: {self._tedavi_bitis}, "
                f"Tedavi Süresi: {self.tedavi_sure()} gün")


