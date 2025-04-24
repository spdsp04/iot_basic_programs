import RPi.GPIO as GPIO
import time
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from collections import deque

# GPIO Setup
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

# GUI Setup
root = tk.Tk()
root.title("Ultrasonic Sensor with Live Graph")
root.geometry("500x400")
root.configure(bg='white')

# Distance Label
label = tk.Label(root, text="Measuring...", font=("Helvetica", 18), bg="white")
label.pack(pady=10)

# Live Graph Setup
max_points = 50
distance_history = deque([0]*max_points, maxlen=max_points)

fig, ax = plt.subplots(figsize=(5, 2.5))
line, = ax.plot(distance_history)
ax.set_title("Distance over Time")
ax.set_ylim(0, 100)
ax.set_ylabel("cm")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()

def update_gui():
    try:
        dist = get_distance()
        label.config(text=f"{dist:.1f} cm")

        # Change label background based on distance
        if dist < 20:
            label.config(bg="red")
        else:
            label.config(bg="green")

        # Update graph data
        distance_history.append(dist)
        line.set_ydata(distance_history)
        line.set_xdata(range(len(distance_history)))
        ax.set_ylim(0, max(max(distance_history)+10, 30))
        canvas.draw()

    except Exception as e:
        label.config(text="Error")
        print("Error:", e)

    root.after(500, update_gui)

def on_close():
    GPIO.cleanup()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

update_gui()
root.mainloop()
