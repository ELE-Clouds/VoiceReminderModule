import network
import time

SSID = "EST8266_Server"
PASSWORD = "micropythoN"


# 设置成热点模式
def apSet(_ssid, _passwd):
    ap = network.WLAN(network.AP_IF)  # 设置为AP模式
    ap.config(essid=_ssid, passwd=_passwd)
    return True


# 设置为客户端模式
def staSet(_ssid, _passwd):
    sta = network.WLAN(network.STA_IF)
    sta.connect(_ssid, _passwd)
    # 查询网络状态
    sta.status()
    return True


def connectWifi(_ssid, _passwd):  # 建立wifi连接
    global wlan
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()
    wlan.connect(_ssid, _passwd)
    count = 0
    while (wlan.ifconfig()[0] == '0.0.0.0'):
        time.sleep(1)
        count += 1
        if count == 30:
            break
    return wlan.ifconfig()[0]
