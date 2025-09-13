import qrcode

# pip install qrcode Pillow

data = "Opa eu sou o Pedro!"

img = qrcode.make(data)

img.save("qrcode_imagem.png")
