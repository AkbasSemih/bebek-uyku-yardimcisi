README.md
# Bebek Uyku Yardımcısı

Bu proje, Python ile geliştirilmiş bir **bulanık mantık tabanlı karar destek sistemidir**. Amaç, bebeklerin uykuya geçişini kolaylaştırmak için çevresel faktörleri analiz ederek uyuma ihtimali ve önerilen desteği sunmaktır.

##  Proje Özellikleri

- **Kullanıcı dostu arayüz** (Tkinter kullanılarak)
- **5 Girdi**: Işık, Sıcaklık, Ses, Aktivite Seviyesi, Son Uyku Süresi (dk)
- **2 Çıktı**: Uyuma İhtimali (%) ve Destek Türü (Sessizlik, Ninni, Ortam Ayarı vb.)
- **Bulanık Mantık** algoritması kullanılarak karar verme
- **Geliştirici dostu** ve kolay genişletilebilir yapı

##  Gerekli Kütüphaneler

```bash
pip install -r requirements.txt
```

##  Kullanım

1. Bu projeyi indir:
    ```bash
    git clone https://github.com/AkbasSemih/bebek-uyku-yardimcisi.git
    cd bebek-uyku-yardimcisi
    ```

2. Gerekli kütüphaneleri yükle:
    ```bash
    pip install -r requirements.txt
    ```

3. Programı başlat:
    ```bash
    python main.py
    ```

##  Nasıl Çalışır?

Arayüzde kullanıcı, çevresel koşulları ve bebeğin son uyku süresini girer. Ardından sistem bu verileri bulanık mantık kurallarıyla değerlendirir ve hem uyuma ihtimalini hem de hangi desteğin daha etkili olacağını kullanıcıya bildirir.

##  Kullanılan Teknolojiler

- Python
- Tkinter
- scikit-fuzzy (Fuzzy Logic)
- Git/GitHub

##  Proje Amacı

Bu proje, üniversite dersi kapsamında yapılmış olup, bulanık mantık uygulaması ile gerçek bir problemi çözmeye yönelik geliştirilmiştir. Özellikle yeni doğan bakımıyla ilgilenen bireyler için pratik bir karar destek sistemi sunmayı amaçlamaktadır.

##  Klasör Yapısı

```
bebek_uyku_yardimcisi/
│
├── main.py               
├── fuzzy_logic.py        
├── requirements.txt      
└── README.md             
```

---

👶 Uykusuz gecelere veda edin! Bu sistemle bebeğinizin uykuya geçiş sürecini daha kolay yönetin.
