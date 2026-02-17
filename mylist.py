#Create afrom machine import PWM, Pin
from machine import Pin
import time

led1 = Pin(33,OUT )
led2 = Pin(26, OUT )
led3 = Pin(19,OUT )
led4 = Pin(22, OUT )

list1 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

for a in my list1:
    led1.value(a[0])
    led2.value(a[1])
    led3.value(a[2])
    led4.value(a[3])
    time.sleep(1)



