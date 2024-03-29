import qrcode
from PIL import Image

logo_file_name = 'logo.png'
data_to_encode = 'Написать текст сюда. Написать текст сюда. Написать текст сюда. '

qr_code = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr_code.add_data(data_to_encode)
qr_code.make()

# qr code image
qr_code_image = qr_code.make_image()

# logo image 
logo = Image.open(logo_file_name)

# populate the position of the logo to center of QR code
logo_x_position = (qr_code_image.size[0] - logo.size[0]) // 2
logo_y_position = (qr_code_image.size[1] - logo.size[1]) // 2
logo_position = (logo_x_position, logo_y_position)

# insert logo image into qr code image
qr_code_image.paste(logo, logo_position)

# save QR code image
qr_code_image.save('qr_with_logo.png')

print('QR code with logo successful generated as qr.png')