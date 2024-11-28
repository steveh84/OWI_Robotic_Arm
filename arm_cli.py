# ROBOT ARM CONTROL - Command line test, Steve Harris

# CREDITS: Based on article "SKUTTER: Part2: How to write a program for your USB device" by Bodge N Hackitt ;-)
#          from The MagPi Magazine, Issue 3.

# import the USB and Time libraries into Python
import usb.core, usb.util, time

# Allocate the name 'RoboArm' to the USB device
RoboArm = usb.core.find(idVendor=0x1267,idProduct=0x0000)

# Check if the arm is detected and warn if not
if RoboArm is None:
    raise ValueError("Arm not found")

# How long to wait between commands
Duration=1

# Define a function to execute a movement
def MoveArm(Duration, ArmCmd):
    # Start the movement
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,1000)
    # Stop movement after waiting specified time
    time.sleep(Duration)

# Give the arm some commands
MoveArm(1,[0,1,0]) # Rotate Base Anti-clockwise
MoveArm(1,[0,2,0]) # Rotate Base Clockwise
MoveArm(1,[64,0,0]) # Shoulder Up
MoveArm(1,[128,0,0]) # Shoulder Down
MoveArm(1,[16,0,0]) # Elbow Up
MoveArm(1,[32,0,0]) # Elbow Down
MoveArm(1,[4,0,0]) # Wrist Up
MoveArm(1,[8,0,0]) # Wrist Down
MoveArm(1,[2,0,0]) # Grip Open
MoveArm(1,[1,0,0]) # Grip Close
MoveArm(1,[0,0,1]) # Light On
MoveArm(1,[0,0,0]) # Light Off