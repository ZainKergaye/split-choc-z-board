from machine import Pin
from time import sleep

led = Pin(24, Pin.OUT)

while True:
    led.value(1)  # Turn the LED on
    sleep(1)      # Wait for 1 second
    led.value(0)  # Turn the LED off
    sleep(1)      # Wait for 1 second
