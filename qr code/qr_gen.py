import qrcode

img = qrcode.make("http://alexarnstein.github.io/donosti_rules")

img.save("qr_code.png")
