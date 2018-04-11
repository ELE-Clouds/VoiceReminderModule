#-*-coding:utf-8-*-

from machine import UART

uart1 = UART(1,9600)
uart1.init(9600,bits=8,parity=None,stop=1,timeout=1000)

def send(_strText):
    uart1.write(_strText)
