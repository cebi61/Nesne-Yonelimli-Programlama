import tkinter as tk

class CalisanYonetimi:
    def __init__(self):
        self.calisanlar = []

    def calisan_ekle(self, calisan):
        self.calisanlar.append(calisan)

    def calisanlari_goster(self):
        for calisan in self.calisanlar:
            print(calisan)

class Uygulama:
    def __init__(self, root):
        self.root = root
        self.root.title("Çalışan Yönetimi")

        self.yonetim = CalisanYonetimi()

        self.ekle_button = tk.Button(root, text="Çalışan Ekle", command=self.calisan_ekle_pencere)
        self.ekle_button.pack(pady=10)

        self.liste_button = tk.Button(root, text="Çalışanları Göster", command=self.calisanlari_goster)
        self.liste_button.pack()

    def calisan_ekle_pencere(self):
        ekle_pencere = tk.Toplevel(self.root)
        ekle_pencere.title("Çalışan Ekle")

        isim_label = tk.Label(ekle_pencere, text="İsim:")
        isim_label.pack()

        isim_entry = tk.Entry(ekle_pencere)
        isim_entry.pack()

        soyisim_label = tk.Label(ekle_pencere, text="Soyisim:")
        soyisim_label.pack()

        soyisim_entry = tk.Entry(ekle_pencere)
        soyisim_entry.pack()

        maas_label = tk.Label(ekle_pencere, text="Maaş:")
        maas_label.pack()

        maas_entry = tk.Entry(ekle_pencere)
        maas_entry.pack()

        ekle_button = tk.Button(ekle_pencere, text="Ekle", command=lambda: self.calisan_ekle(isim_entry.get(), soyisim_entry.get(), maas_entry.get(), ekle_pencere))
        ekle_button.pack()

    def calisan_ekle(self, isim, soyisim, maas, pencere):
        calisan = f"{isim} {soyisim} - Maaş: {maas}"
        self.yonetim.calisan_ekle(calisan)
        pencere.destroy()

    def calisanlari_goster(self):
        liste_pencere = tk.Toplevel(self.root)
        liste_pencere.title("Çalışan Listesi")

        for calisan in self.yonetim.calisanlar:
            label = tk.Label(liste_pencere, text=calisan)
            label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = Uygulama(root)
    root.mainloop()
