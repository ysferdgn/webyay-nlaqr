# qr code oluştur
import qrcode

# QR koduna dönüştürülecek URL
url = "http://localhost:8000/baglantilarim.html"



# QR kodu oluşturma
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# QR kodunu bir resim dosyasına kaydetme
img = qr.make_image(fill='black', back_color='white')
img.save("qr_code.png")


#qr ı aç
from PIL import Image

# QR kodunu açma
img = Image.open("qr_code.png")
img.show()
