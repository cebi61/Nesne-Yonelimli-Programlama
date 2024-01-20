def kuvvet_al(x,y): #Positional arguments kaç adet atadıysak o kadar veri girilmeli
    return x**y

# print(kuvvet_al(3,4))

def bilgi_ver(ad,soyad = "Girilmedi",yas="Girilmedi"): #Keyword argument
    return f"Ad: {ad} Soyad: {soyad} Yas: {yas}"

# print(bilgi_ver("Ali","Çalışkan","23"))

def bilgi_ver2(ad = "Girilmedi",soyad = "Girilmedi",yas="Girilmedi"): #Keyword argument
    return f"Ad: {ad} Soyad: {soyad} Yas: {yas}"

# print(bilgi_ver2(soyad="çalışkan"))


def topla2(x,y):
    return x + y

def topla3(x,y,z):
    return x + y + z

def topla(*args):
    for arg in args:
        print(arg)

# topla(1,2,3,4,5,"Python",True)
        
def carp(*args):
    carpim = 1
    for arg in args:
        carpim *= arg
    return carpim

# print(carp(2,3,4,5))


def ortalama(*args):
    return sum(args) / len(args)

# print(ortalama(5,8,10,17))



def selamla(mesaj, *args):
    sonuc = ""
    sonuc += mesaj
    sonuc += " "
    for arg in args:
        sonuc += arg
        sonuc += " "
    return sonuc

# print(selamla("Merhaba", "Ali", "Nasılsın"))


def fonk(**kwargs):
    print(kwargs)

# fonk(ad = "ali", soyad = "çalışkan", yas = 34)
    

def fonk2(zorunlu, *args, **kwargs):
    print(zorunlu)
    print("**************")
    for arg in args:
        print(arg)
    print("***************")
    for k,v in kwargs.items():
        print(k,v)

fonk2(2, 3, 4, 5, 6, 7, ad="Ali", yas=23)





