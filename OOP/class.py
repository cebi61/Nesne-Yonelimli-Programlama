class calisan:
    def __init__(self, name, surname = "girilmedi", age = 0):
        self.name = name
        self.surname = surname
        self.age = age
    def show_info(self):
        print(f"Ad:{self.name}  Soyad: {self.surname}   Yaş: {self.age}")

calisan1 = calisan("Ali","Veli",20)
calisan2 = calisan("Ahmet","Mehmet",25)
calisan3 = calisan("Kerem")

calisan1.show_info()
calisan2.show_info()
calisan3.show_info()


