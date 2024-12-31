

import qrcode

website_link = 'https://www.bing.com/search?q=Vidhanasouda&form=SWAUA2'


qr = qrcode.QRCode(
    version=1,  
    box_size=5, 
    border=20    
)

qr.add_data(website_link)  
qr.make(fit=True)  


img = qr.make_image(fill_color="black", back_color="white")
img.save("QRcodeimg.png")

