from gpiozero import CPUTemperature
import subprocess
import sys
import Adafruit_DHT
import telepot
import os
import time,threading

timer_mex = 300
threshold = 1.5
threshold_temp_str = str(threshold)
sensor = Adafruit_DHT.DHT11
pin=4

#array for associate person to Telegram code
bot_codes = {"Diego Corradi" : "xxxxxxxx"}

#try to send message on Telegram, in case of error retry after 3 seconds, otherwise send error message
def bot_send(text):
 for id_name, id_bot in bot_codes.items():
  try:
   bot.sendMessage(chat_id=id_bot, text=text)
  except:
   time.sleep(3)
   try:
    bot.sendMessage(chat_id=id_bot, text=text)
   except:
    print("Error on sending BOT Telegram message to " + id_name + " .")

#check threshold of temperature
def check_temp_filed():
    threading.Timer(timer_mex, check_temp_filed).start()
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if(temperature < threshold):
        temperature = str(temperature)
        humidity = str(humidity)
        body = "Temperature: " +  temperature + "°C\n" + "Humidity: " + humidity + "%"
        bot_send(body)

#menu of bot
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    #get of the sent message
    command=msg['text']
 
    if content_type == 'text':
        if command == '/info_temp':
            bot.sendMessage(chat_id,'Temperature: {0:0.01f}°C \nHumidity: {1:0.01f}%'.format(temperature, humidity))
        if command == '/info_raspy':
            cpu = CPUTemperature()
            temp = str(cpu.temperature)
            str1 = 'Temperature Raspberry: '
            str_fin = str1 + temp + '°C'
            bot.sendMessage(chat_id,str_fin)
        if command == '/info_notifications':
            str_notifiche = 'Check Temperature: '
            str_tempnotifiche = str(timer_mex)
            str_not1 = str_notifiche + str_tempnotifiche + 's\n'
            str_not_soglia = 'Soglia: ' + str(threshold) + '°C'
            str_fin = str_not1 + str_not_soglia
            bot.sendMessage(chat_id,str_fin)
        if command == '/settings_admin':
           bot.sendMessage(chat_id,'MENU ADMIN\n\n1)Info Temperature: /info_temp\n2)Info Raspberry: /info_raspy\n3)Info Notifications: /info_notifications\n4)Admin settings: /settings_admin\n5)Shutdown: /shutdown6)Reboot: /reboot\n')
        if command == '/shutdown':
            bot.sendMessage(chat_id,'Shutdown Raspberry!')
            os.system('sudo shutdown now')
        if command == '/reboot':
            bot.sendMessage(chat_id,'Reboot Raspberry!')
            os.system('sudo shutdown -r now')

#token of bot
TOKEN = '12346789:xxxxxxx'

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)
print ('Listening ...')
bot.sendMessage(xxxxxxxx,'Raspberry ready!')
check_temp_filed()

while 1:
    time.sleep(1)
