import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc): # MQTT 연결 subscribe 시작 
    print("Connected with result code "+str(rc))
    client.subscribe("/demd")

def on_message(client, userdata, msg): # MQTT에서 수신한 메시지 출력
    print(msg.payload.decode())

client = mqtt.Client()
broker="MQTT SERVER IP" # "MQTT SERVER IP"에는 mqtt서버의 IP주소를 입력
client.connect(broker,1883,60)

client.on_connect = on_connect # MQTT 수신 시작 
client.on_message = on_message # 수신한 메시지 출력 

client.loop_forever()  # 무한 반복 