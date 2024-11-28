# OWI_Robotic_Arm
Python code samples for the USB version of the OWI Robotic Arm, including PowerPoint slides demonstrating how the commands to control the robotic arm are broken down into binary. This code was developed on a Raspberry Pi 400 using Python v3.9.2 and based on the article "SKUTTER: Part2: How to write a program for your USB device" by Bodge N Hackitt from The MagPi Magazine, Issue 3.

# Contents
### RobotArm.pptx
This is a PowerPoint slides identifying the purpose of the chips on the controller. 

![image](https://github.com/user-attachments/assets/3d106362-8f2e-4177-b16f-546ab6990800)

An animated slide is also included with a brief introduction to binary/bits/bytes as well as demonstrating how the integer values in the code represent binary values understood by the chips.

![image](https://github.com/user-attachments/assets/690fde17-7229-4d43-b7d7-0175e146c575)


Also included is an animated slide demonstrating the meaning of the integer values which are passed to the robotic arm through the USB driver in the Python code.

![image](https://github.com/user-attachments/assets/6a770a31-337e-4765-bf94-7b0d032ef226)

### `arm_cli.py`
This code will automatically move each of the components of the arm in either direction and turn the LED light on and off with a 1 second delay between each action. No user interaction is provided in this code. This is useful for testing communication with the arm and checking all the components on the arm.

### `arm_gui.py`
A simple graphical user interfaces to control the robotic arm, created with PyAT5. A text entry box is provided to control how long each movement last for. Separate buttons are provided for moving each joint in the arm in each direction as well as separate buttons for turning the LED light on and off.

# Requirements
`arm_cli.py` requires the python `usb` package.

`arm_gui.py` requires the python `usb, sys, PyQt5` packages.

# Use in the Classroom
This can be an interesting and applied method for introducing binary and the difference between what humans find readable and what machines find readable as well as the concepts of bits and bytes. 

I have also found it interesting to ask the students why they think so many bits in byte 2 and 3 are unused. Surely it is a waste to have what are essentially overpowered chips runing this robotic arm? Why not combine the information in byte 3 into byte 2 and eliminate the resources needed for byte 3?

One potential answer is that it may have been too expensive to have a chip specifically designed and manufactured for this particular arm. Instead, it was cheaper to use commonly available chips, which while overpowered for this allication, they would be cheaper to buy as they are bulk produced. *I do not know if this is actually the reason but it is a fair assumption and can just make students aware of the potential re-use of electronic components across many applications.*

# Acquiring the OWI Robotic Arm
The OWI Robotic Arm I used here was purchased many years ago and is the USB version. I am not sure if the USB version can be purchased anymore, but I have seen a manually controlled version of this arm available on [Amazon](https://www.amazon.co.uk/Build-Your-Own-Robot-Arm/dp/B00OXL0VUQ/ref=asc_df_B00OXL0VUQ?mcid=e860bc86b005368fa789f0ca0351e519&hvadid=697314515024&hvpos=&hvnetw=g&hvrand=9804245845520405180&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9045081&hvtargid=pla-564353859993&psc=1&gad_source=1) and a seperate [USB conversion kit](https://www.fuze.co.uk/store/p102/USB_interface_Kit_for_OWI_Robotic_Arm.html) which looks like it replaces the controller board in the base of the arm (I do not benefit from these links).
