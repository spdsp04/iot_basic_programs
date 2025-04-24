import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24
LED = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()
    stop = time.time()

    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        stop = time.time()

    return ((stop - start) * 34300) / 2

try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist:.1f} cm")

        if dist < 20:
            GPIO.output(LED, GPIO.HIGH)
        else:
            GPIO.output(LED, GPIO.LOW)

        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
