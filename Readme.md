语音提醒模块<BR>——Voice Reminder Module
===
简介<BR>
---
语音提醒模块主要分为定时提醒与外部触发两种事件模式。
<BR>

KT603C管脚说明
<BR>

| 引脚序号 | 引脚名称 | 功能描述 | 备注        |
|:--------:|:--------:|:-------- |:----------- |
| 1        | DACL     | 左声道   |             |
| 2        | DACR     | 右声道   |             |
| 3        | 3V3      | 3.3V 稳压输出 |        |
| 4        | VIN      | 电源输入   |           |
| 5        | GND      | 电源地   |             |
| 6        | TX       | 通用输入输出口 | 串口的发送脚 |
| 7        | RX       | 通用输入输出口 | 串口的接收脚 |
| 8        | X1       | 晶振输入   | 可以做GPIO |
| 9        | X2       | 晶振输出   | 可以做GPIO |
| 10       | INT/GPIOA0 | 通用输入输出口 | 外部中断[低电平触发] |
| 11       | GPIOA1   | 通用输入输出口   | SPI的输入 |
| 12       | GPIOA2   | 通用输入输出口   | SPI的时钟 |
| 13       | GPIOA3   | 通用输入输出口   | SPI的输出 |
| 14       | GPIOA4   | 通用输入输出口   |           |
| 15       | GPIOA5   | 通用输入输出口   |           |
| 16       | GPIOA6   | 通用输入输出口   |           |
| 17       | GPIOB4   | 通用输入输出口   | SDCLK     |
| 18       | GPIOB3   | 通用输入输出口   | SDCMD     |
| 19       | GPIOB2   | 通用输入输出口   | SDDAT     |
| 20       | GPIOB1   | 通用输入输出口   | USB-      |
| 21       | GPIOB0   | 通用输入输出口   | USB+      |
| 22       | RST      | 复位脚           | 复位脚    |
| 23       | VCOM     | DAC 的参考电压   | DAC 的参考电压 |
| 24       | DACVSS   | DAC 的输出地     | DAC 的输出地 |

<BR>

RTC实时时钟模块：<BR>

RTC.datetime(datetime)
*设置与获取当前时间*
datetime格式：(year,month,day,weekday(0~6),hour,minute,second,yearday(1~366))
不带参数时为获取时间


RTC.memory
*RTC存储器*


RTC.alarm(id, time, *, repeat=False)
*设置闹钟时间*
time:闹钟时间，其值为当前时间的毫秒值+未来时间的毫秒值
repeat:是否循环

RTC.alarm_left(alarm_id=0)
*获取闹钟到期之前剩余的毫秒数*


RTC.irq(*, trigger, handler=None, wake=machine.IDLE)
*创建一个由 RTC.alarm 触发的irq对象。*
trigger:触发器
handler:回调函数
wake:中断可以唤醒系统的睡眠模式

RTC.ALARM0
*常量*
irq 触发源


网络对时功能
ntptime

host

time

settime

