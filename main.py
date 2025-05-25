# main.py
import tkinter as tk
from tkinter import messagebox
from fuzzy_logic import hesapla

def hesapla_sonuc():
    try:
        # Kutular boş mu kontrolü
        if not all([entry.get().strip() for entry in girisler]):
            raise ValueError("Boş alan bırakmayın.")

        # Girişleri al
        isik = int(entry_isik.get())
        sicaklik = int(entry_sicaklik.get())
        ses = int(entry_ses.get())
        aktivite = int(entry_aktivite.get())
        uyku_suresi = int(entry_uyku.get())

        # Mantıklı aralıkta mı kontrol
        if not (0 <= isik <= 100 and 15 <= sicaklik <= 30 and 0 <= ses <= 100 and 0 <= aktivite <= 10 and uyku_suresi >= 0):
            raise ValueError("Değer aralıklarını kontrol edin.")

        # Hesaplama
        uyuma, destek = hesapla(isik, sicaklik, ses, aktivite, uyku_suresi)

        # Destek açıklaması
        destek_map = {
            0: "Sessizlik",
            1: "Ninni",
            2: "Ortam Ayarı",
            3: "Destek Gerekmez"
        }

        lbl_sonuc.config(text=f"Uyuma İhtimali: %{uyuma:.1f}\nDestek: {destek_map.get(destek, 'Bilinmiyor')}", fg="green")

    except ValueError as ve:
        messagebox.showwarning("Uyarı", str(ve))
    except Exception as e:
        print("Hata:", e)  # CMD ekranında detay görmek için
        messagebox.showerror("Hata", "Beklenmeyen bir hata oluştu.")

# Arayüz
pencere = tk.Tk()
pencere.title("Bebek Uyku Yardımcısı")
pencere.geometry("300x250")

etiketler = ['Işık (0-100)', 'Sıcaklık (15-30)', 'Ses (0-100)', 'Aktivite (0-10)', 'Son uyku süresi (dk)']
girisler = []

for i, etiket in enumerate(etiketler):
    tk.Label(pencere, text=etiket).grid(row=i, column=0, padx=5, pady=5, sticky="e")
    entry = tk.Entry(pencere)
    entry.grid(row=i, column=1, padx=5, pady=5)
    girisler.append(entry)

entry_isik, entry_sicaklik, entry_ses, entry_aktivite, entry_uyku = girisler

tk.Button(pencere, text="Hesapla", command=hesapla_sonuc).grid(row=6, column=0, columnspan=2, pady=10)

lbl_sonuc = tk.Label(pencere, text="", fg="blue")
lbl_sonuc.grid(row=7, column=0, columnspan=2)

pencere.mainloop()
