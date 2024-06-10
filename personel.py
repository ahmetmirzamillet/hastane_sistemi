class Personel:
    def __init__(self,personel_no,ad,soyad,departman,maas):
        self._personel_no = personel_no
        self._ad = ad
        self._soyad = soyad
        self._departman = departman
        self._maas =maas

    def get_personel_no(self):
        return self._personel_no

    def set_personel_no(self,personel_no):
        self._personel_no = personel_no

    def get_ad(self):
        return self._ad

    def set_ad(self,ad):
        self._ad = ad

    def get_soyad(self):
        return self

    def set_soyad(self,soyad):
        self._soyad = soyad

    def get_departman(self):
        return self._departman

    def set_departman(self, departman):
        self._departman=departman

    def get_maas(self):
        return self._maas

    def __str__(self):
        return  f"Personel no: {self._personel_no} ad: {self._ad} soyad: {self._soyad} departman: {self._departman} maas: {self._maas} "

