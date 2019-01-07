from pyfirmata import Arduino, util # firmata를 이용해 python코드로 아두이노 조작
from time import sleep  


# usb에 연결된 아두이노와 연결 
board = Arduino('/dev/ttyACM0')
it = util.Iterator(board)  
it.start()


# 아두이노 조작 2가지 방법 
# 1. 
#board.analog[0].enable_reporting() 
#board.analog[0].read()

# 2. 
digital_LED = board.get_pin('d:11:o') # ( d , a ):pin_num:( i , o ) d:digital a:analog  / i: input o: output 
digital_LED.write(1) # light 켜기
sleep(3)
digital_LED.write(0) # light 끄기
#pin3 = board.get_pin('d:3:p')
#pin3.write(0.6)

