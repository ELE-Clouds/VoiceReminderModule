from oled096 import *
from rtcfw import *
from netConnect import *
from ntp import *
from machine import Timer,Pin

SSID = 'NTS'
PASSWORD = 'nanjingtiansu'

flsOled()
olDesplay(('Connecting...',0,32))

#连接wifi网络
IP = connectWifi(SSID,PASSWORD)
if IP != '0.0.0.0':
    flsOled()
    olDesplay(('WLAN Successful!', 0, 32))
    #print("网络连接成功！")
    # 系统启动时NTP时间同步一次
    while not setTime():
        #print("NTP时间同步失败，重新同步！")
        sleep(1)

else:
    flsOled()
    olDesplay(('WLAN Failed!', 0, 32))
    #print('网络连接失败！')
    sleep(1)



#引脚电位初始化
Pin(12).value(0)
Pin(13).value(0)


#屏幕显示
def dateView():
    strDate,strWe,strTime = getTime()
    dateView = '%.2d-%.2d-%.2d'%strDate
    timeView = '%.2d:%.2d'%strTime
    dstm = 'AC: %.2d:%.2d:%.2d'%(lstimeDS[3:6])
    flsOled()
    olDesplay((dateView,0,12))
    olDesplay((timeView,0,24))
    olDesplay((dstm,0,40))
    olDesplay(('IP:'+IP, 0, 55))

#显示屏幕
dateView()


#每小时NTP时间同步一次
tim1 = Timer(1)
tim1.init(period=3600000, mode=Timer.PERIODIC, callback=lambda t:setTime())

#每10秒刷新一次屏幕
tim2 = Timer(2)
tim2.init(period=10000, mode=Timer.PERIODIC, callback=lambda t:(timeJy(lstimeDS),dateView()))

