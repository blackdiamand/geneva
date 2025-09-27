import RPi.GPIO as GPIO
from time import sleep
import tkinter as tk

GPIO.setwarnings(False)

# Right Motor (Motor A)
in1 = 17
in2 = 27
en_a = 4
# Left Motor (Motor B)
in3 = 5
in4 = 6
en_b = 13
# Motor C
in1_c = 15
in2_c = 18
en_c = 14
# Motor D
in3_d = 16
in4_d = 20
en_d = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en_a,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en_b,GPIO.OUT)

GPIO.setup(in1_c,GPIO.OUT)
GPIO.setup(in2_c,GPIO.OUT)
GPIO.setup(en_c,GPIO.OUT)

GPIO.setup(in3_d,GPIO.OUT)
GPIO.setup(in4_d,GPIO.OUT)
GPIO.setup(en_d,GPIO.OUT)

q=GPIO.PWM(en_a,100)
p=GPIO.PWM(en_b,100)
r=GPIO.PWM(en_c,100)
s=GPIO.PWM(en_d,100)
p.start(75)
q.start(75)
r.start(75)
s.start(75)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in1_c,GPIO.LOW)
GPIO.output(in2_c,GPIO.LOW)
GPIO.output(in3_d,GPIO.LOW)
GPIO.output(in4_d,GPIO.LOW)

# Create GUI
root = tk.Tk()
root.title("Motor Control")
root.geometry("300x500")

# Status label to display motor actions
status_label = tk.Label(root, text="Motor Status: Stopped", font=("Arial", 12))
status_label.pack(pady=10)

def left_forward():
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    status_label.config(text="Left Motor Forward (B)")

def left_backward():
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    status_label.config(text="Left Motor Backward (B)")

def right_forward():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    status_label.config(text="Right Motor Forward (A)")

def right_backward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    status_label.config(text="Right Motor Backward (A)")

def motor_c_forward():
    GPIO.output(in1_c,GPIO.HIGH)
    GPIO.output(in2_c,GPIO.LOW)
    status_label.config(text="Motor C Forward")

def motor_c_backward():
    GPIO.output(in1_c,GPIO.LOW)
    GPIO.output(in2_c,GPIO.HIGH)
    status_label.config(text="Motor C Backward")

def motor_d_forward():
    GPIO.output(in3_d,GPIO.HIGH)
    GPIO.output(in4_d,GPIO.LOW)
    status_label.config(text="Motor D Forward")

def motor_d_backward():
    GPIO.output(in3_d,GPIO.LOW)
    GPIO.output(in4_d,GPIO.HIGH)
    status_label.config(text="Motor D Backward")

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in1_c,GPIO.LOW)
    GPIO.output(in2_c,GPIO.LOW)
    GPIO.output(in3_d,GPIO.LOW)
    GPIO.output(in4_d,GPIO.LOW)
    status_label.config(text="Stop")

# Create buttons
btn_right_forward = tk.Button(root, text="Right Forward (e) - Motor A", command=right_forward, width=20)
btn_right_forward.pack(pady=5)

btn_right_backward = tk.Button(root, text="Right Backward (d) - Motor A", command=right_backward, width=20)
btn_right_backward.pack(pady=5)

btn_left_forward = tk.Button(root, text="Left Forward (w) - Motor B", command=left_forward, width=20)
btn_left_forward.pack(pady=5)

btn_left_backward = tk.Button(root, text="Left Backward (s) - Motor B", command=left_backward, width=20)
btn_left_backward.pack(pady=5)

btn_motor_c_forward = tk.Button(root, text="Motor C Forward (r)", command=motor_c_forward, width=20)
btn_motor_c_forward.pack(pady=5)

btn_motor_c_backward = tk.Button(root, text="Motor C Backward (f)", command=motor_c_backward, width=20)
btn_motor_c_backward.pack(pady=5)

btn_motor_d_forward = tk.Button(root, text="Motor D Forward (t)", command=motor_d_forward, width=20)
btn_motor_d_forward.pack(pady=5)

btn_motor_d_backward = tk.Button(root, text="Motor D Backward (g)", command=motor_d_backward, width=20)
btn_motor_d_backward.pack(pady=5)

btn_stop = tk.Button(root, text="Stop (c)", command=stop, width=20)
btn_stop.pack(pady=5)

# Handle window close
def on_closing():
    GPIO.cleanup()
    print("GPIO Clean up")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

try:
    root.mainloop()
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Clean up")
