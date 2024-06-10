import personel#personel sınıfı eklendi

class Hemşire(personel.Personel):#personel sınıfı kalıtım yolu ile eklendi
    def __init__(self,personel_no,ad,soyad,departman,maas,çalışma_saati,serttifika,hastane):
        personel.Personel.__init__(self,personel_no,ad,soyad,departman,maas)
        self._çalışma_saati=çalışma_saati
        self._serttifika=serttifika
        self._hastane=hastane

    def maas_arttır(self,new_maas):#maas arttır metodu eklendi.
        self._maas+=new_maas

    def get_çalışma_saati(self):
        return self._çalışma_saati
    def set_çalışma_saati(self,çalışma_saati):
        self._çalışma_saati=çalışma_saati

    def get_serttifika(self):
        return self._serttifika
    def set_serttifika(self,serttifika):
        self._serttifika=serttifika

    def get_hastane(self):
        return self._hastane
    def set_hastane(self,hastane):
        self._hastane=hastane

    def __str__(self):
        return f"{super().__str__()}/Çalışma_saati={self._çalışma_saati}/serttifika={self._serttifika}/hastane={self._hastane}"
