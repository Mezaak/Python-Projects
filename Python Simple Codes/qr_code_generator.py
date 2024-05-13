import qrcode
from PIL import Image

# Veri
data = "https://www.openai.com/"

# QR kodu oluştur
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# QR kodunu PIL görüntüsü olarak al
img = qr.make_image(fill_color="black", back_color="white")

# PIL görüntüsünü numpy dizisine dönüştür
img_np = img.getdata()

# Renkleri değiştir
new_colors = [(210, 255, 0) if pixel == 0 else (0, 255, 0) for pixel in img_np]
img.putdata(new_colors)

# Yeni renklerle QR kodunu kaydet
file_path = "qr_code_with_colors.png"
img.save(file_path)

print(f"QR kodu başarıyla oluşturuldu ve '{file_path}' dosyasına kaydedildi.")

