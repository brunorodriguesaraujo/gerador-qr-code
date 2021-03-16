import pyqrcode

#exemplo de link: 'https://www.instagram.com/brunorodrig_es/'
link = str(input("Digite seu link: "))
pyqrcode.create(link).svg('qrcode.svg', scale=5)

