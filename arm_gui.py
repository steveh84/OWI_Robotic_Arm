# ROBOT ARM CONTROL - with pyQt UI, Steve Harris

# CREDITS: Based on article "SKUTTER: Part2: How to write a program for your USB device" by Bodge N Hackitt ;-)
#          from The MagPi Magazine, Issue 3.
#          I have added a simple user interface to provide individual buttons for each control

# Developed on: Python v3.9.2, Raspberry Pi (Developed on a Pi 400)
# on Raspberry Pi execute this script from command line, from the source folder: sudo python arm.py

# Requirements
# - pyUSB http://goo.gl/5GbcD
# - PyQT5

# - ARM can only move one motor at a tim, due to sleep(), combined commands do not execute

# import the PyQT5, USB and Time libraries into Python
import sys
import usb.util, time
from PyQt5.QtWidgets import *


class Window(QDialog):
    # Check the Robot arm exists
    roboarm = usb.core.find(idVendor=0x1267, idProduct=0x0000)

    # Check if the arm is detected and warn if not
    if roboarm is None:
        raise ValueError("Arm not found")

    # set the length of time each command will execute for
    duration = 1

    # Time to leve light on for, use a fail-safe so light not left on permanently
    light_duration = 1

    # Byte commands to control each part of robot arm
    clockwise = [0, 1, 0]  # Byte command to rotate Base Anti-clockwise
    anti_clockwise = [0, 2, 0]  # Byte command to rotate Base Clockwise
    shoulder_up = [64, 0, 0]  # Byte command to move shoulder Up
    shoulder_down = [128, 0, 0]  # Byte command to move shoulder Down
    elbow_up = [16, 0, 0]  # Byte command to move elbow Up
    elbow_down = [32, 0, 0]  # Byte command to move elbow Down
    wrist_up = [4, 0, 0]  # Byte command to move wrist Up
    wrist_down = [8, 0, 0]  # Byte command to move wrist Down
    grip_open = [2, 0, 0]  # Byte command to move grip Open
    grip_close = [1, 0, 0]  # Byte command to move grip Close
    light_on = [0, 0, 1]  # Byte command to move light On
    light_off = [0, 0, 0]  # Byte command to move light Off

    # Main method to move the arm, recieves 3 vector input for the 3 byte command structre
    def MoveArm(self, cmd, duration):
        # Start the movement
        self.roboarm.ctrl_transfer(0x40, 6, 0x100, 0, cmd, 1000)

        # Stop movement after waiting specified time
        print(self.timeEdit.text())
        duration = float(self.timeEdit.text())
        time.sleep(duration)
        cmd = [0, 0, 0]
        self.roboarm.ctrl_transfer(0x40, 6, 0x100, 0, cmd, 1000)

    # When a click event occurs on a PyQT push button, the 'click' event needs to connect to a specific function
    # A function for each button therefore needs to be created to run the relevent code for that button, these are listed below

    # Move the arm clockwise
    def MoveClockwise(self):
        self.MoveArm(self.clockwise, self.duration)

    # Move the arm anti_clockwise
    def MoveAntiClockwise(self):
        self.MoveArm(self.anti_clockwise, self.duration)

    # Move the shoulder_up
    def MoveShoulderUp(self):
        self.MoveArm(self.shoulder_up, self.duration)

    # Move the arm shoulder_down
    def MoveShoulderDown(self):
        self.MoveArm(self.shoulder_down, self.duration)

    # Move the arm elbow_up
    def MoveElbowUp(self):
        self.MoveArm(self.elbow_up, self.duration)

    # Move the elbow_down
    def MoveElbowDown(self):
        self.MoveArm(self.elbow_down, self.duration)

    # Move the wrist_up
    def MoveWristUp(self):
        self.MoveArm(self.wrist_up, self.duration)

    # Move the elbow_down
    def MoveWristDown(self):
        self.MoveArm(self.wrist_down, self.duration)

    # Move the grip_open
    def GripOpen(self):
        self.MoveArm(self.grip_open, self.duration)

    # Move the grip_close
    def GripClose(self):
        self.MoveArm(self.grip_close, self.duration)

    # Move the light_on
    def LightOn(self):
        # Leave light on for longer using 'light on time'
        self.MoveArm(self.light_on, self.light_duration)

    # Move the light_off
    def LightOff(self):
        self.MoveArm(self.light_off, self.duration)

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # these two lines apply the sizePolicy to the button to stop it resizing across the window
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # TIME textbox
        self.timeEdit = QLineEdit(self)
        # Apply the sizePolicy to text box to stop it resizing across the window
        size_policy.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(size_policy)
        # This line links the button to another function which will be called when the button is clicked
        self.timeEdit.setText("1")
        self.timeLabel = QLabel("Duration",self)

        # CLOCKWISE button
        self.clockWiseButton = QPushButton('Rotate Clockwise')
        # Apply the sizePolicy to button to stop it resizing across the window
        size_policy.setHeightForWidth(self.clockWiseButton.sizePolicy().hasHeightForWidth())
        self.clockWiseButton.setSizePolicy(size_policy)
        # This line links the button to another function which will be called when the button is clicked
        self.clockWiseButton.clicked.connect(self.MoveClockwise)

        # ANTI-CLOCKWISE button
        self.antiClockWiseButton = QPushButton('Rotate Anti-Clockwise')
        # Apply the sizePolicy to button to stop it resizing across the window
        size_policy.setHeightForWidth(self.antiClockWiseButton.sizePolicy().hasHeightForWidth())
        self.antiClockWiseButton.setSizePolicy(size_policy)
        # This line links the button to another function which will be called when the button is clicked
        self.antiClockWiseButton.clicked.connect(self.MoveAntiClockwise)

        # SHOULDER UP button
        self.shoulderUpButton = QPushButton('Shoulder Up')
        # Apply the sizePolicy to button to stop it resizing across the window
        size_policy.setHeightForWidth(self.shoulderUpButton.sizePolicy().hasHeightForWidth())
        self.shoulderUpButton.setSizePolicy(size_policy)
        # This line links the button to another function which will be called when the button is clicked
        self.shoulderUpButton.clicked.connect(self.MoveShoulderUp)

        # SHOULDER DOWN button
        self.shoulderDownButton = QPushButton('Shoulder Down')
        # Apply the sizePolicy to button to stop it resizing across the window
        size_policy.setHeightForWidth(self.shoulderDownButton.sizePolicy().hasHeightForWidth())
        self.shoulderDownButton.setSizePolicy(size_policy)
        # This line links the button to another function which will be called when the button is clicked
        self.shoulderDownButton.clicked.connect(self.MoveShoulderDown)

        # ELBOW UP button
        self.elbowUpButton = QPushButton('Elbow Up')
        # Apply the sizePolicy to button to stop it resizing across the window
        size_policy.setHeightForWidth(self.elbowUpButton.sizePolicy().hasHeightForWidth())
        self.elbowUpButton.setSizePolicy(size_policy)
        # This line links the button to another function which will be called when the button is clicked
        self.elbowUpButton.clicked.connect(self.MoveElbowUp)

        # ELBOW DOWN button
        self.elbowDownButton = QPushButton('Elbow Down')
        # Apply the sizePolicy to button to stop it resizing across the window
        size_policy.setHeightForWidth(self.elbowDownButton.sizePolicy().hasHeightForWidth())
        self.elbowDownButton.setSizePolicy(size_policy)
        # This line links the button to another function which will be called when the button is clicked
        self.elbowDownButton.clicked.connect(self.MoveElbowDown)

        # WRIST UP button
        self.wristUpButton = QPushButton('Wrist Up')
        # Apply the sizePolicy to button to stop it resizing across the window
        size_policy.setHeightForWidth(self.wristUpButton.sizePolicy().hasHeightForWidth())
        self.wristUpButton.setSizePolicy(size_policy)
        # This line links the button to another function which will be called when the button is clicked
        self.wristUpButton.clicked.connect(self.MoveWristUp)

        # WRIST DOWN button
        self.wristDownButton = QPushButton('Wrist Down')
        # Apply the sizePolicy to button to stop it resizing across the window
        size_policy.setHeightForWidth(self.wristDownButton.sizePolicy().hasHeightForWidth())
        self.wristDownButton.setSizePolicy(size_policy)
        # This line links the button to another function which will be called when the button is clicked
        self.wristDownButton.clicked.connect(self.MoveWristDown)

        # GRIP OPEN button
        self.gripOpenButton = QPushButton('Grip Open')
        # Apply the sizePolicy to button to stop it resizing across the window
        size_policy.setHeightForWidth(self.gripOpenButton.sizePolicy().hasHeightForWidth())
        self.gripOpenButton.setSizePolicy(size_policy)
        # This line links the button to another function which will be called when the button is clicked
        self.gripOpenButton.clicked.connect(self.GripOpen)

        # GRIP CLOSE button
        self.gripCloseButton = QPushButton('Grip Close')
        # Apply the sizePolicy to button to stop it resizing across the window
        size_policy.setHeightForWidth(self.gripCloseButton.sizePolicy().hasHeightForWidth())
        self.gripCloseButton.setSizePolicy(size_policy)
        # This line links the button to another function which will be called when the button is clicked
        self.gripCloseButton.clicked.connect(self.GripClose)

        # LIGHT ON button
        self.lightOnButton = QPushButton('Light On')
        # Apply the sizePolicy to button to stop it resizing across the window
        size_policy.setHeightForWidth(self.lightOnButton.sizePolicy().hasHeightForWidth())
        self.lightOnButton.setSizePolicy(size_policy)
        # This line links the button to another function which will be called when the button is clicked
        self.lightOnButton.clicked.connect(self.LightOn)

        # LIGHT OFF button
        self.lightOffButton = QPushButton('Light Off')
        # Apply the sizePolicy to button to stop it resizing across the window
        size_policy.setHeightForWidth(self.lightOffButton.sizePolicy().hasHeightForWidth())
        self.lightOffButton.setSizePolicy(size_policy)
        # This line links the button to another function which will be called when the button is clicked
        self.lightOffButton.clicked.connect(self.LightOff)

        # Create a grid layout
        grid_layout = QGridLayout()
        grid_layout.spacing = 5

        # Add label for duration to col 1st column
        grid_layout.addWidget(self.timeLabel, 0, 0)
        # Add text entry for durationa dn all other buttons to second column
        grid_layout.addWidget(self.timeEdit, 0,1)
        grid_layout.addWidget(self.clockWiseButton, 1, 1)
        grid_layout.addWidget(self.antiClockWiseButton, 2, 1)
        grid_layout.addWidget(self.shoulderUpButton, 3, 1)
        grid_layout.addWidget(self.shoulderDownButton, 4, 1)
        grid_layout.addWidget(self.elbowUpButton, 5, 1)
        grid_layout.addWidget(self.elbowDownButton, 6, 1)
        grid_layout.addWidget(self.wristUpButton, 7, 1)
        grid_layout.addWidget(self.wristDownButton, 8, 1)
        grid_layout.addWidget(self.gripOpenButton, 9, 1)
        grid_layout.addWidget(self.gripCloseButton, 10, 1)
        grid_layout.addWidget(self.lightOnButton, 11, 1)
        grid_layout.addWidget(self.lightOffButton, 12, 1)
        self.setLayout(grid_layout)

# The main application
if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
