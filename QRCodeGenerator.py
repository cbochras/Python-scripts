import qrcode
#pip install qrcode
# prompt the user for input
data = input("Enter data to encode: ")

# create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# add data to the QR code
qr.add_data(data)

# generate the QR code image
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# save the image file
img.save("qrcode.png")
