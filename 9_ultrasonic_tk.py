import RPi.GPIO as GPIO
import time
import tkinter as tk

# GPIO Pins
TRIG = 23
ECHO = 24

# GPIO Setup
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

# GUI Setup
root = tk.Tk()
root.title("Ultrasonic Sensor Distance")
root.geometry("300x150")
root.configure(bg='white')

label = tk.Label(root, text="Measuring...", font=("Helvetica", 24), bg="white")
label.pack(expand=True)

def update_distance():
    try:
        dist = get_distance()
        label.config(text=f"{dist:.1f} cm")

        # Change background color based on proximity
        if dist < 20:
            label.config(bg="red")
        else:
            label.config(bg="green")

    except Exception as e:
        label.config(text="Error")
        print("Error:", e)

    root.after(500, update_distance)

# Start the loop
update_distance()

def on_close():
    GPIO.cleanup()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
