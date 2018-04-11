#-*-coding:utf-8-*-

import network
import time

# 连接WIFI
def connectWifi(_ssid, _passwd):
    global wlan
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()
    wlan.connect(_ssid, _passwd)
    while (wlan.ifconfig()[0] == '0.0.0.0'):
        time.sleep(1)
    return wlan.ifconfig()[0]
