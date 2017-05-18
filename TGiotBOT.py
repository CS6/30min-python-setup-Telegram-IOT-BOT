##加入溫度監控
#可直接使用的BOT
#V1
#!/usr/bin/env python3
#-*- coding: utf-8 -*-



#app = Flask(__name__)

#logging.basicConfig(level=logging.DEBUG,

#                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#bot_name = '@aboutbig6bot'

#bot = telegram.Bot(token='344519590:AAH1Gzn260TvJRHclFPBGW8S1mmBPNJW8Gw')

#~/workcode/telepot/examples/chat
#TEXT = '您好'

#bot.sendMessage(chat_id='-230670018', text='我是新人')
#bot.sendMessage(chat_id='-230670018', text=TEXT)
#bot.setWebhook("https://sddivid.tw")  
#https://api.telegram.org/bot344519590:AAH1Gzn260TvJRHclFPBGW8S1mmBPNJW8Gw/sendMessage?chat_id=@big666bot&text=test
#curl https://api.telegram.org/bot344519590:AAH1Gzn260TvJRHclFPBGW8S1mmBPNJW8Gw/setWebhook?url=sean.taipei/telegram/hook.php
#https://api.telegram.org/bot344519590:AAH1Gzn260TvJRHclFPBGW8S1mmBPNJW8Gw/getUpdates

#@app.route('/<token>', methods=['POST'])
##Day2##
from datetime import datetime
import time,datetime
##Day2##
import serial
import sys
from telegram.ext import Updater  
from telegram.ext import CommandHandler

#name = input('請輸入你的名稱：')
#print('歡迎 ', name)
#設定時間戳記&格式化日期
DD=time.strftime("%Y-%m-%d--%H:%M:%S")
DT=time.strftime("%Y-%m-%d--%H:%M:%S") 

print(DT)
print(DD)
#請用 [ls /dev] 查詢要用的PORT
ser = serial.Serial('/dev/ttyACM6', 9600)#arduino板01
#ser = serial.Serial('/dev/ttyAMA0', 9600)#arduino板01
#讀取一行
data = ser.readline()
print (data)  
#datb = data.encode()
#print (datb)

print ("Good bye!")

#token 輸入 bot father 給你的 bot 專屬 token key
updater = Updater(token='輸入你的');  
dispatcher = updater.dispatcher

#start 方法
def start(bot, update):  
    bot.sendMessage(chat_id=update.message.chat_id, text="安安你好我是大六")
    bot.sendMessage(chat_id=update.message.chat_id, text="很高興認識你")

def info(bot, update):  
    bot.sendMessage(chat_id=update.message.chat_id, text="作者:sddivid")
    bot.sendMessage(chat_id=update.message.chat_id, text="GitHub:才不告訴你")
    bot.sendMessage(chat_id=update.message.chat_id, text="Telegram:@sddivid")


def server(bot, update):  
    bot.sendMessage(chat_id=update.message.chat_id, text="溫度C/溫度F/濕度")
    datb = str(data)
    #使用str(  )將讀入的數值轉為字串
    bot.sendMessage(chat_id=update.message.chat_id, text="數值"+ datb)
   
    print (data)  #檢查用
    bot.sendMessage(chat_id=update.message.chat_id, text=datb)
    print (datb) #檢查用





#第一個參數是接受的指令 `\start` 的字串。
start_handler = CommandHandler('start',start)
#第2個參數是接受的指令 `\info` 的字串。
info_handler = CommandHandler('info',info)
#第3參數是接受的指令 `\info` 的字串。
server_handler = CommandHandler('server',server)


#告訴 api 增加一個新的指令處理方法 (註冊)
dispatcher.add_handler(start_handler)
#告訴 api 增加2個新的指令處理方法 (註冊)
dispatcher.add_handler(info_handler)
#告訴 api 增加3個新的指令處理方法 (老師}
dispatcher.add_handler(server_handler)

updater.start_polling()  



#########################
##
##一個參數是接受的指令 `\start` 的字串。
#start -1
##第2個參數是接受的指令 `\info` 的字串。
#info -2
##第3參數是接受的指令 `\info` 的字串。
#teacher -3
##第4參數是接受的指令 `\info` 的字串。
#professor -4
##第5參數是接受的指令 `\info` 的字串。
#stu -5
##第6參數是接受的指令 `\info` 的字串。
#talk -6
##第7參數是接受的指令 `\info` 的字串。
#aboutme -7
#########
'''
start - 1A
info - 2A
teacher - 3A
professor - 4A
stu - 5A
talk - 6A
aboutme - 7A
server - 8A
order - 9A


ser.read(1)  # 小括號內可以填入一次要讀取的byte數

ser.readline()  # 讀取一列資料直到換行符號

ser.readlines()  # 讀取全部的資料

ser.readline(decode())
讀取進來的資料為Byte，要處理成字串的話記得加上decode()


ser.write('3')

大概就是RPI 傳送  3 出去....
pi@raspberrypi:/etc/workspace/tgbot/mybot1 $ sudo python3 mybot2.py

'''
##########################
