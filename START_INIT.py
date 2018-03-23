from oled096 import *
from rtcfw import *
from netConnect import *
from ntp import *
from machine import Timer,Pin

SSID = 'NTS'
PASSWORD = 'nanjingtiansu'

#连接wifi网络
IP = connectWifi(SSID,PASSWORD)
print("网络连接成功！")

#系统启动时NTP时间同步一次
setTime()
print("时间同步成功，开始初始化引脚！")

#引脚电位初始化
Pin(12).value(0)
Pin(13).value(0)


#屏幕显示
def dateView():
    strDate,strWe,strTime = getTime()
    dateView = str(strDate[0])+'-'+str(strDate[1])+'-'+str(strDate[2])
    timeView = str(strTime[0])+':'+str(strTime[1])
    dstm = 'AC: %d:%d:%d'%(lstimeDS[3:6])
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