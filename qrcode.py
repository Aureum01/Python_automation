#import as qr code 
import qrcode
input = 'https://youtu.be/dQw4w9WgXcQ'
qr = qrcode.QRCode(
  version=1,
  bs= 10,
  border=5)
qr.add_data(input)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save(training.png)
