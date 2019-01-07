# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

mqttc = mqtt.Client('python1') 
mqttc.connect("MQTT SERVER IP", 1883, 60) # "MQTT SERVER IP"에는 mqtt서버의 IP주소를 입력
mqttc.publish("/demd", "안녕하세요") # "/demd" : 송신할 토픽 , "안녕하세요" : 송신할 내용
mqttc.disconnect();