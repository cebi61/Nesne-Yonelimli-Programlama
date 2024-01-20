#__str__ ve __repr__

# a = "Python"
# print(str(a))
# print(repr(a))
#_____________________________________________
# from datetime import date
# import datetime

# bugun = date.today()
# print(bugun)
# print(str(bugun))
# print(repr(bugun))

# c = datetime.date(2024, 1, 20)
#_____________________________________________

class Futbolcu:
    def __init__(self,isim,soyisim,yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
    
    def __str__(self):
        return f"Ad: {self.isim} Soyad: {self.soyisim} Yaş: {self.yas}"
    
    def __repr__(self):
        return f'Futbolcu("{self.isim}","{self.soyisim}",{self.yas})'
    
futbolcu1 = Futbolcu("Ali","Veli",20)

print(futbolcu1)
print(futbolcu1.__repr__())