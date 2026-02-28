# Importing library
from operator import pos

import qrcode
from PIL import Image
 
# Data to be encoded == Link yg ingin dibuat QR Code nya
data = 'https://s.id/LINK'

# Membuat QR dengan error correction tinggi
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=2,
)

qr.add_data(data)
qr.make(fit=True)

img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Buka logo
logo = Image.open("logo.png")

# Resize logo (misal 1/4 ukuran QR)
qr_width, qr_height = img_qr.size
logo_size = qr_width // 4
logo = logo.resize((logo_size, logo_size))

# Posisi kiri atas
posisi = (30, 27)

# Tempel logo
img_qr.paste(logo, posisi, mask=logo if logo.mode == 'RGBA' else None)

# Simpan hasil
img_qr.save("Hasil_logo.png")