# libary yang digunakan untuk membuat QR code
import qrcode
from PIL import Image, ImageDraw

data = "https://s.id/FromTheorytoMethod"

# Buat QR dengan error correction tinggi
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=3,
)

qr.add_data(data)
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

# Buka logo (PNG transparan)
logo = Image.open("logo.png").convert("RGBA")
logo = logo.resize((logo_size, logo_size))

# Tempel logo di tengah
qr_img.paste(logo, (x, y), logo)

# nama file hasil
qr_img.save("LinkDaftarSC8.png")