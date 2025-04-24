import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

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

    elapsed = stop - start
    distance = (elapsed * 34300) / 2  # in cm
    return distance

try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist:.1f} cm")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
