from machine import I2C,Pin
from ssd1306 import SSD1306_I2C

i2c = I2C(sda=Pin(5),scl=Pin(4))
oled = SSD1306_I2C(128,64,i2c)

#显示文字
def olDesplay(_lsText):
    oled.text(_lsText[0],_lsText[1],_lsText[2])
    oled.show()

#刷新屏幕
def flsOled():
    oled.fill(0)

