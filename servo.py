import time
from adafruit_servokit import ServoKit

# Initialize the ServoKit library with 16 channels.
kit = ServoKit(channels=16)

# Select the servo on channel 0.
servo = kit.servo[0]

# Turn the servo to 180 degrees.
servo.angle = 180
print("Servo turned to 180 degrees.")

# Wait for 3 seconds.
time.sleep(3)

# Turn the servo to 0 degrees.
servo.angle = 0
print("Servo returned to 0 degrees.")