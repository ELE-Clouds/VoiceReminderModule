import ntptime
from utime import localtime,sleep
from machine import RTC

NTPHOST = ('cn.ntp.org.cn','edu.ntp.org.cn','time.windows.com')

ntptime.host = NTPHOST[0]

#同步时钟
def setTime():
    # 补时间差8小时
    lsTime=[]
    for i in range(3):
        lsTime.insert(i,localtime(ntptime.time()))
        #print(lsTime[i][3:5])
        sleep(1)
    if lsTime[0][3:5] == lsTime[1][3:5] and lsTime[0][3:5] == lsTime[2][3:5] and lsTime[1][3:5] == lsTime[2][3:5]:
        t = ntptime.time() + 28800
        tm = localtime(t)
        tm = tm[0:3] + (0,) + tm[3:6] + (0,)
        RTC().datetime(tm)
        return True
    return False
