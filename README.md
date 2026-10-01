# 📌 Custom QR Code Generator with Logo

A Python-based QR Code Generator that allows you to embed a custom logo in the center of the QR code, manage target URLs securely via `.env`, and dynamically name output files.

---

## ✨ Fitur Utama

- 🔗 **Input Link Dinamis**: URL / data tujuan diinputkan langsung secara mandiri dan interaktif melalui terminal ke dalam variabel, tanpa harus statis di file `.env`.
- 🖼️ **Logo di Tengah (Center Logo)**: Menyematkan logo di bagian tengah QR Code secara presisi dan proporsional dengan clear area (kotak putih latar).
- 🛡️ **High Error Correction (`ERROR_CORRECT_H`)**: Menggunakan level koreksi kesalahan tertinggi (~30%), memastikan QR Code tetap terbaca sempurna oleh scanner meski ada logo di tengahnya.
- 📂 **Penyimpanan Dinamis**: Nama file output dapat ditentukan langsung melalui terminal saat script dijalankan, tersimpan otomatis di dalam folder `Output/`.

---

## 📁 Struktur Direktori

```text
QR-CODE/
├── .gitignore          # Daftar file/folder yang diabaikan Git
├── logo.png            # File logo yang akan disematkan di tengah QR Code (opsional)
├── qr.py               # Script utama generator QR Code
├── README.md           # Dokumentasi proyek
├── requirements.txt    # Daftar dependensi library Python
└── Output/             # Folder tempat file QR Code disimpan (diabaikan oleh git)
```

---

## 🚀 Panduan Penggunaan

### 1. Kloning Repository
```bash
git clone https://github.com/Narendra238/QR-CODE.git
cd QR-CODE
```

### 2. Instalasi Dependensi
Pastikan Python sudah terpasang di komputer Anda. Pasang library yang dibutuhkan dengan perintah:
```bash
pip install -r requirements.txt
```

### 3. Siapkan File Logo (Opsional)
Tempatkan file gambar logo Anda dengan nama `logo.png` di folder utama (root proyek) atau `Output/Logo.png`.  
> *Rekomendasi: Gunakan file PNG dengan latar transparan berukuran persegi (1:1).*

### 4. Jalankan Program
Jalankan script Python:
```bash
python qr.py
```

Anda akan diminta menginputkan link dan nama file hasil secara langsung:
```text
Masukkan link : https://s.id/YourLinkHere
Link yang dimasukkan: https://s.id/YourLinkHere
Masukkan nama file hasil (contoh: LinkBaru): MyQRCode
Membuat QR Code untuk: https://s.id/YourLinkHere
 Berhasil disimpan di: Output\MyQRCode.png
```

File hasil QR Code akan otomatis tersimpan di folder `Output/`.

---

## 🛠️ Dependensi

- [qrcode](https://pypi.org/project/qrcode/) - Generator QR Code
- [Pillow (PIL)](https://pypi.org/project/pillow/) - Pengolahan gambar dan manipulasi logo
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Membaca konfigurasi dari file `.env`

---

## 👤 Penulis

Dibuat oleh **[Narendra238](https://github.com/Narendra238)**.
