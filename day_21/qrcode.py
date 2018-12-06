# coding:utf-8

import qrcode

img = qrcode.make("雪娜我爱你")
img.save("test.png")
print("hello")
