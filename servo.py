import time
from adafruit_servokit import ServoKit

# Initialize the ServoKit library with 16 channels.
kit = ServoKit(channels=16, address=0x42)

# Select the servos on channels 0 and 1.
servo1 = kit.servo[0]
servo2 = kit.servo[1]

# Set initial positions
servo1.angle = 180
servo2.angle = 85
time.sleep(1)

# New sequence
print("Step 1: Servo 1 to 180")
servo1.angle = 0
time.sleep(1)

print("Step 2: Servo 2 to 0")
servo2.angle = 40
time.sleep(1)

print("Step 3: Servo 1 to 0")
servo1.angle = 180
time.sleep(1)

print("Step 4: Servo 2 to 90")
servo2.angle = 110
time.sleep(1)

print("Step 5: Servo 1 to 180")
servo1.angle = 0
time.sleep(1)

print("Step 6: Servo 1 to 0")
servo1.angle = 180
time.sleep(1)

print("Step 7: Servo 2 to 0")
servo2.angle = 85
time.sleep(1)
