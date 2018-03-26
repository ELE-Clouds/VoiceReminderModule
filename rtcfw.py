from machine import RTC,Pin
from utime import localtime,sleep_ms,sleep

lstimeDS = (localtime()[0:3]+(8,43,0)+localtime()[6:9])

#引脚定义
beep = Pin(14, Pin.OUT)
beep.value(0)

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
        Beep()

#闹铃
def Beep():
    #print("闹铃响！")
    beep.value(0)
    LEDG.value(1),LEDR.value(0)

    for i in range(30):
        beep.value(not beep.value())
        LEDG.value(not LEDG.value())
        LEDR.value(not LEDR.value())
        sleep_ms(500)
        LEDG.value(not LEDG.value())
        LEDR.value(not LEDR.value())
        sleep_ms(500)
    beep.value(0)
    LEDG.value(0)
    LEDR.value(0)
    #print("闹铃关闭！")
    sleep(1)

