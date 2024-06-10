import personel

class Doktor(personel.Personel):
    def __init__(self,personel_no,ad,soyad,departman,maas,uzmanlık,deneyim_yılı,hastane):
        personel.Personel.__init__(self,personel_no,ad,soyad,departman,maas)
        self._uzmanlık=uzmanlık
        self._deneyim_yılı=int(deneyim_yılı)
        self._hastane=hastane

    def get_uzmanlık(self):
        return self._uzmanlık

    def set_uzmanlık(self,uzmanlık):
        self._uzmanlık=uzmanlık

    def get_deneyim_yil(self):
        return self._deneyim_yılı

    def set_deneyim_yil(self,deneyim_yil):
        self._deneyim_yil=int(deneyim_yil)

    def get_hastane(self):
        return self._hastane

    def set_hastane(self,hastane):
        self._hastane=hastane


    def maas_arttır(self,new_maas):
        self._maas=new_maas

    def __str__(self):
        return f"{super().__str__()}, Uzmanlık:{self._uzmanlık}, Deneyim:{self._deneyim_yılı}, Hastane:{self._hastane}"

