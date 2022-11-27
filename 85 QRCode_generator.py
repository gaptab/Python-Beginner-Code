import pyqrcode
import png
data="https://play.google.com/store/apps/dev?id=6855554087523421165"
qr=pyqrcode.create(data)

qr.png('Seventysevenapps.png',scale=5)