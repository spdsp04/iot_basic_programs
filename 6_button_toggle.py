import RPi.GPIO as GPIO
import time

LED_PIN = 17
BUTTON_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

led_state = False

def toggle_led(channel):
    global led_state
    led_state = not led_state
    GPIO.output(LED_PIN, led_state)

GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=toggle_led, bouncetime=300)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
