import network
import time
def connectWifi(_ssid, _passwd):  # 寤虹珛wifi杩炴帴
    global wlan
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()
    wlan.connect(_ssid, _passwd)
    while (wlan.ifconfig()[0] == '0.0.0.0'):
        time.sleep(1)
    return wlan.ifconfig()[0]
