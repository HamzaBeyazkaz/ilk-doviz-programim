import tkinter as tk
from tkinter import messagebox
import requests

def hesapla():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        # İnternetten veriyi çek
        cevap = requests.get(url)
        veri = cevap.json()
        kur = veri["rates"]["TRY"]
        
        # Kullanıcının girdiği miktarı al
        miktar = float(entry_miktar.get())
        sonuc = miktar * kur
        
        # Sonucu ekrandaki etikete yazdır
        label_sonuc.config(text=f"Sonuç: {sonuc:.2f} TL", fg="green")
        label_kur.config(text=f"Anlık Kur: {kur:.2f}")
        
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")
    except Exception as e:
        messagebox.showerror("Bağlantı Hatası", "Kura ulaşılamadı!")

# 1. Ana Pencereyi Oluştur
pencere = tk.Tk()
pencere.title("Gece Kodlaması: Döviz Botu v2.0")
pencere.geometry("350x250")

# 2. Görsel Öğeleri Ekle
tk.Label(pencere, text="Dolar Miktarını Girin:", font=("Arial", 12)).pack(pady=10)

entry_miktar = tk.Entry(pencere, font=("Arial", 14))
entry_miktar.pack(pady=5)

btn_hesapla = tk.Button(pencere, text="HESAPLA", command=hesapla, bg="blue", fg="white", font=("Arial", 10, "bold"))
btn_hesapla.pack(pady=20)

label_kur = tk.Label(pencere, text="Kur bekleniyor...", font=("Arial", 10))
label_kur.pack()

label_sonuc = tk.Label(pencere, text="", font=("Arial", 14, "bold"))
label_sonuc.pack(pady=10)

# 3. Pencereyi Açık Tut
pencere.mainloop()