https://wokwi.com/projects/458675361252738049

from machine import Pin
from utime import sleep
import sys

print("Hello, ESP32!")

red = Pin(15, Pin.OUT)
blue = Pin(12, Pin.OUT)

red.value(0)
blue.value(0)

while True:
    user_input = input("Type (blue), (red) or (f) to shut down: ").lower().strip()

    if user_input == "red":
        red.value(1)
        blue.value(0)
        sleep(1)
        print("Red LED is ON!")

    elif user_input == "blue":
        red.value(0)
        blue.value(1)
        sleep(1)
        print("Blue LED is ON!")

    elif user_input == "f":
        print("Shutting down ESP32.")
        sleep(0.8)
        print("Shutting down ESP32..")
        sleep(0.8)
        print("Shutting down ESP32...")
        sleep(0.3)
        red.value(0)
        blue.value(0)
        sys.exit()

    else:
        print(f"You typed: {user_input}")
        print("Error: Please use only 'blue' or 'red'")
