#-*-coding:utf-8-*-

#指定文件播放报文编码
playJh = b'\x7E\xFF\x06\x0F\x00\x07\x01\xEF'
playDd = b'\x7E\xFF\x06\x0F\x00\x07\x02\xEF'

# PTUF1FS_V2.4 模块通讯协议
# 软件版本 KT603C[SSOP24],主芯片：KT403[SSOP24]
# 通讯标准：9600bps/data:8/stop:1/other:none

# 格式： $s VER Len CMD Freeback para1 para2 checksum $0

'''
    $S:起始位0x7E（每条命令反馈均以$开头，即0x7E）
    VER:版本（版本信息0xFF）
    Len:len后字节个数（校验和不计算在内）
    CMD:命令字（表示具体的操作，比如播放/暂停等等）
    Feedback:命令反馈（是否需要反馈信息，1反馈，0不反馈）
    dat:参数（和前面的len相关联，不限制长度）
    checksum:校验和[占两个字节]（累加和校验[不计起始位$]）
    $0:结束位（结束位0xEF）
    
    校验和计算：0-checksum=校验数据(接收端)，not(checksum)+1=校验数据（发送端）
    
    MCU晶振建议：11.0592MHz或者倍数
'''

# 控制命令
NEXT = 0x01        #下一曲
PREVIOUS = 0x02
SPECIFY_THE_TRACK = 0x03
VOLUME+ = 0x04
VOLUME- = 0x05
SPECIFY_VOLUME = 0x06
SLOOP_SPECIFY_TRACKPL = 0x08 #单曲循环指定曲目播放
SPECIFY_DEVICE = 0x09
ENTER_SLEEP       =   0x0A
WAKE_SLEEP      = 0x0B
RESET       = 0x0C
PLAY    = 0x0D
PAUSE   = 0x0E
SPECIFY_FF_NAME_PLAY = 0x0F
LOOP_ALL_FILES = 0x11
IN_STREAM_ADS = 0x13
ONE_FOLDER_SUPPORTS_1000 = 0x14
STOP_INSERTING_BACKGROUND_MUSIC = 0x15
STOP = 0x16
SPECIFIED_FOLDER_LOOP = 0x17
SPECIFIED_ROOT_RANDOMLY_PLAY = 0x18
SET_CURRENT_LOOP = 0x19
COMBINED_PLAY = 0x21
MULTIPLE_FLOLDER_INSERTIONS = 0x25
SPECIFIED_FOLDER_RANDOM_PLAY = 0x28





# 查询命令


# 反馈标志

class kt603c(object):
