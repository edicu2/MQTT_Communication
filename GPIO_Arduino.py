#coding: utf-8

#GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# time 라이브러리 임포트
import time


# 핀 번호 할당 방법은 커넥터 핀 번호로 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#사용할 핀 번호 할당
LED = 11

# 11번 핀을 출력 핀으로 설정, 초기 출력은 로우 레벨
print("setup")
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
#예외처리 
try:
    #무한반복
    while 1:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.5)
        print("working out")
        
except KeyboardInterrupt:
    GPIO.cleanup ()
    
print("clean up")
GPIO.cleanup ()

