# telegram_bot-temperature

<br>

## Table of Contents

1. [General Info](#general-info)
    - [Getting Started](#getting-started)
    - [Technologies](#technologies)
    - [Dependencies](#dependencies)
2. [Setup](#setup)
3. [Useful Links](#useful-links)

<br>

### General Info

This is a simple telegram bot hosted by a Raspberry Pi 3B+ equipped with a temperature and humidity sensor(DHT11).<br>
The script checks every 5 minutes if the temperature is below a predefined temperature threshold, 
if the condition is true the bot will send a custom message.


#### Getting Started

What I used?

- [Raspberry Pi 3B+](https://www.amazon.it/gp/product/B07BDR5PDW/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) and charger (with Raspberry Pi OS Lite installed)
- [DHT11](https://www.amazon.it/gp/product/B00K67YJ18/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) (temperature and humidity sensor)
- [10k Resistor](https://www.amazon.it/gp/product/B0087ZDQQ0/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- [Wire Connectors](https://www.amazon.it/gp/product/B076F4R6HN/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) (3 jumpers)
- [Breadboard](https://www.amazon.it/gp/product/B01J3M07T4/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- Micro-SD Card 8GB

<img src="https://user-images.githubusercontent.com/32736570/148848577-85239cce-0457-4b2f-9372-3ba24487963d.png" alt="DH11_scheme" width="400" />

<br>

#### Technologies
Created with:
* Python
* Bash Linux

#### Dependencies
* [Adafruit DHT](https://github.com/adafruit/Adafruit_Python_DHT/)

<br>

### Setup
<br>
1) **Telegram Bot Creation**

- Open Telegram and search "BotFather" 

  <img src="https://user-images.githubusercontent.com/32736570/148848683-7968167b-913c-4690-89ad-1395e809da7a.jpg" alt="Bot_Telegram" width="300" />

- To create a new bot, type "/newbot";

- Choose a name for your Bot, type the name and then press Enter;

- Enter a username that will make it recognizable. Username must end in "Bot" or "_bot";

- Once the name is confirmed, we will be notified of the bot token.

<br>

2. **Clone the Adafruit library**

```
sudo apt-get update
sudo apt-get install git-core
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo apt-get install python3-pip
pip3 install telepot
cd examples
```

Now we can try to test the code with the command:

```
python3 ./Adafruit_Python_DHT.py 11 4
```

<br>

3. **Improvements of IoT Project**

In a second time, I have improved the script code (simple_bot_DHT.py) with :

- **gpiozero** library, to control the temperature of Raspberry's CPU;
- **os** library to handle shutdown and restart Raspberry;
- **time** library to handle time-related tasks;
- **threading** library to repeat a function every 'n' seconds; 
- **menu** with many options to improve user experience;
- run script as **service**.

<br>

4. **Other Tips**

```
nohup python simple_bot_DHT.py	         //script in background
ps ax | grep simple_bot_DHT.py	         //understand the process to be terminated
ps -ef |grep nohup			            //return PID nohup process
sudo service simple_bot_DHT.py start     //start the service
sudo service simple_bot_DHT.py stop		//stop the service
sudo service simple_bot_DHT.py status	//return status of service		
```

<br>

#### **Useful Links**

https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/

https://francoz.me/dht11-sensor-on-raspberry-pi2-gdocs-logging/

https://www.moreware.org/wp/blog/2020/12/13/raspberry-sensore-dht-11-con-invio-dati-su-telegram/

https://www.caronteconsulting.com/notizie/caronte-consulting/eseguire-script-python-servizio/

<br>

#### License

The MIT License (MIT)

Copyright © 2014 Adafruit Industries
