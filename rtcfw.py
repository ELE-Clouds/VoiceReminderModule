from machine import RTC,Pin
from utime import localtime,sleep_ms,sleep
from uart import *
from KT603C import *

lstimeDS = (localtime()[0:3]+(8,44,0)+localtime()[6:9])

#引脚定义
LEDR = Pin(12, Pin.OUT)
LEDG = Pin(13, Pin.OUT)
LEDG.value(0), LEDR.value(0)

#获取并格式化时间
def getTime():
    rtc = RTC()
    t = rtc.datetime()
    day = (t[0:3])
    week = (t[3])
    tm = (t[4:6])
    return day,week,tm

#设置定时
#def setDS(_lsSet):

#校验
def timeJy(_lsTime):
    #print("开始时间校验！")
    tm = getTime()
    if tm[2] == _lsTime[3:5]:
        YY()


def YY():
    LEDG.value(1)
    for i in range(3):
        send(playJh)
        sleep(8)
    send(playDd)
    sleep(2)
    LEDG.value(0)
    sleep(50)