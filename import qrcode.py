import qrcode
f=qrcode.QRCode(version=1,box_size=40,border=3)
f.add_data('https://github.com/AhmedBI96')
f.make(fit=True)
gi=f.make_image(fill_color="blu")
gi.save('E:\generate qr code\git.png')