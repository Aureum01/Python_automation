import qrcode
from io import BytesIO

# Create the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('This is the data for the QR code')
qr.make(fit=True)

# Save the QR code as an image
img = qr.make_image()

# Create a BytesIO object
buf = BytesIO()

# Save the image to the BytesIO object
img.save(buf, 'PNG')

# Create the HTTP response object
response = HttpResponse(buf.getvalue(), content_type="image/png")

# Set the response headers
response['Content-Disposition'] = 'attachment; filename=qr_code.png'

# Return the response
return response
