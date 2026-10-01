import os
import qrcode
from PIL import Image, ImageDraw

# Input link secara langsung dan dinamis dari user
link = input("Masukkan link : ").strip()

# Validasi agar link tidak kosong
while not link:
    print("Error: Link tidak boleh kosong!")
    link = input("Masukkan link : ").strip()

print(f"Link yang dimasukkan: {link}")

# Input dinamis nama file output dari user
file_name = input("Masukkan nama file hasil (contoh: LinkBaru): ").strip()
if not file_name:
    file_name = "hasil_qr"

# Tambahkan ekstensi .png jika user belum menyertakannya
if not file_name.lower().endswith(".png"):
    file_name += ".png"

# Pastikan folder Output/ tersedia
output_dir = "Output"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, file_name)

print(f"Membuat QR Code untuk: {link}")

# Buat QR dengan error correction tinggi
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=3,
)

qr.add_data(link)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Ukuran QR
qr_w, qr_h = qr_img.size

# Ukuran area logo
logo_size = qr_w // 5

# Posisi tengah
x = (qr_w - logo_size) // 2
y = (qr_h - logo_size) // 2

# Buat kotak putih di tengah (clear area)
draw = ImageDraw.Draw(qr_img)
draw.rectangle((x, y, x + logo_size, y + logo_size), fill="white")

# Buka logo (cek logo.png di root atau di Output/Logo.png)
logo_path = "logo.png" if os.path.exists("logo.png") else os.path.join("Output", "Logo.png")
if os.path.exists(logo_path):
    logo = Image.open(logo_path).convert("RGBA")
    logo = logo.resize((logo_size, logo_size))
    # Tempel logo di tengah
    qr_img.paste(logo, (x, y), logo)
else:
    print(f"Peringatan: File logo tidak ditemukan di '{logo_path}'. QR code dibuat tanpa logo.")

# Simpan hasil QR Code
qr_img.save(output_path)
print(f" Berhasil disimpan di: {output_path}")