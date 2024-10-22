import pyfirmata
import time

# Connect to the Arduino board
comport = '/dev/cu.usbmodem211201'

board = pyfirmata.Arduino(comport)
it = pyfirmata.util.Iterator(board)
it.start()

# Define the pins
led_pin1 = board.get_pin('d:11:o')
led_pin2 = board.get_pin('d:10:o')
led_pin3 = board.get_pin('d:9:o')
led_pin4 = board.get_pin('d:6:o')
led_pin5 = board.get_pin('d:5:o') 

# function to turn on the LED based on the number of fingers
def turn_on_led(fingers):
    if fingers == 0:
        led_pin1.write(0)
        led_pin2.write(0)
        led_pin3.write(0)
        led_pin4.write(0)
        led_pin5.write(0)
    elif fingers == 1:
        led_pin1.write(1)
        led_pin2.write(0)
        led_pin3.write(0)
        led_pin4.write(0)
        led_pin5.write(0)
    elif fingers == 2:
        led_pin1.write(1)
        led_pin2.write(1)
        led_pin3.write(0)
        led_pin4.write(0)
        led_pin5.write(0)
    elif fingers == 3:
        led_pin1.write(1)
        led_pin2.write(1)
        led_pin3.write(1)
        led_pin4.write(0)
        led_pin5.write(0)
    elif fingers == 4:
        led_pin1.write(1)
        led_pin2.write(1)
        led_pin3.write(1)
        led_pin4.write(1)
        led_pin5.write(0)
    elif fingers == 5:
        led_pin1.write(1)
        led_pin2.write(1)
        led_pin3.write(1)
        led_pin4.write(1)
        led_pin5.write(1)



