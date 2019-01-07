import smbus
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
from pyfirmata import Arduino, util


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc): # MQTT 수신 
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/demd")  
    
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):  # MQTT 수신 메시지 추력 및 기타 동작 
    print(msg.topic+" "+msg.payload.decode())
    led_controll(4)
    bus = smbus.SMBus(1)
    v = check_temperature()
    T = v / 3.1
    print ("T = %4.1f centigrades" %T)
    if msg.payload.decode() == "led":
        print(0)
        digital_LED.write(1)
        time.sleep(3)
        digital_LED.write(0)
    else :
        print(1)
        while True:
            voltage = analog_temp.read()
            temp = 5.0*100*voltage
            print(temp)
    pin3 = board.get_pin('d:3:p')
    pin3.write(0.6)


    
def check_temperature(port = 0):  #주위 온도 파악 
    if port == 0:
        adc_address = 0x48
    elif port == 1:    
        adc_address = 0x4D
    rd = bus.read_word_data(adc_address, 0)
    data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
    data = data >> 2
    return data
    
def led_controll(second):   #LED 조작 함수 
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    LED = 11
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(second)
    GPIO.cleanup ()

board = Arduino('/dev/ttyACM0')
it = util.Iterator(board)
it.start()

# 아두이노 조작 2가지 방법 
# 1.
#board.analog[0].enable_reporting()
#board.analog[0].read()

# 2.
digital_LED = board.get_pin('d:11:o')
analog_temp = board.get_pin('a:0:i')


broker="MQTT SERVER IP" # "MQTT SERVER IP"에는 mqtt서버의 IP주소를 입력
client = mqtt.Client("python1") 
client.on_connect = on_connect  # MQTT 수신 시작
client.on_message = on_message  # 수신했을 때 message 출력 및 기타 동작 

client.connect(broker, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
 
