import ntptime
from utime import localtime
from machine import RTC

NTPHOST = ('cn.ntp.org.cn','edu.ntp.org.cn')

ntptime.host = NTPHOST[0]

#同步时钟
def setTime():
    # 补时间差8小时
    t = ntptime.time() + 28800
    tm = localtime(t)
    tm = tm[0:3] + (0,) + tm[3:6] + (0,)
    RTC().datetime(tm)
