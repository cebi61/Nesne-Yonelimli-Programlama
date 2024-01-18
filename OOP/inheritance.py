class Calisan:
    zam_orani = 1.1

    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"

    def bilgileri_goster(self): 
        return "Ad: {} Soyad: {} Maas: {} Email: {}".format(self.isim, self.soyisim, self.maas, self.email)

calisan1 = Calisan("Ali", "Çalışkan", 5000)
calisan2 = Calisan("Veli", "Uzun", 6000)


class Yazilimci(Calisan):
    def __init__(self, isim, soyisim, maas, bildigi_dil):
        super().__init__(isim, soyisim, maas)
        self.zam_orani = 1.2
        self.bildigi_dil = bildigi_dil

    def bilgileri_goster(self):
        return "Ad: {} Soyad: {} Maas: {} Email: {} Dil: {}".format(self.isim, self.soyisim, self.maas, self.email, self.bildigi_dil)


Yazilimci1 = Yazilimci("Ayşe", "Yıldız", 7000, "Java")
Yazilimci2 = Yazilimci("Fatma", "Ay", 8000, "Python")


class Yonetici(Calisan):
    def __init__(self, isim, soyisim, maas,calisanlar = None):
        super().__init__(isim, soyisim, maas)
        if calisanlar == None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar
    def calisan_ekle(self,calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)
    def calisan_sil(self,calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)
    def calisanlari_goster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgileri_goster())

yonetici1 = Yonetici("Metin","Ali",10000)
yonetici2 = Yonetici("Feyyaz","Beşiktaş",11000,[Yazilimci1,Yazilimci2,calisan1])
# yonetici2.calisanlari_goster()

print(isinstance(yonetici2,Calisan)) #nesnenin o class tan türeyip türemediğine bakıyor
print(issubclass(Yazilimci,Calisan)) #clasın o clas tan türeyip türemediğine bakıyor 




# yonetici1.calisan_ekle(calisan1)
# yonetici1.calisan_ekle(Yazilimci1)
# yonetici1.calisanlari_goster()
# print("****************")
# yonetici1.calisan_sil(calisan1)
# yonetici1.calisanlari_goster()
