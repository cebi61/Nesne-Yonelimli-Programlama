import tkinter as tk

def buton_tiklandi():
    metin = entry.get()
    label.config(text="Girilen Metin: " + metin)

# Ana uygulama penceresi
app = tk.Tk()
app.title("Görsel Programlama Örneği")

# Metin kutusu
entry = tk.Entry(app, width=30)
entry.pack(pady=10)

# Düğme
button = tk.Button(app, text="Tıkla", command=buton_tiklandi)
button.pack()

# Etiket
label = tk.Label(app, text="")
label.pack(pady=10)

# Uygulamayı çalıştır
app.mainloop()
