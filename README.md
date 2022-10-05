# motorised_curtain
***The cheapest smart curtain that compatible with iPhone and Siri***

This could be a part of the smart home that you can control the curtain to open and close on your phone (Apple's iPhone). 
This project involves with mechanical parts which you need to 3D print out the parts that I have created.
A DC motor is installed to the 3D printed motor holder and installed on to the curtain.
The motor is connected to a RPi with a motor driver. 
Using the Shortcut app on the iPhone, 2 shortcuts are needed which allows Python program runs trough SSH. The Python program checks the input from SSH, checks the state of the curtain (opened/closed) and triggers the motor to spin. 
Siri can be used to trigger the Shortcut which means it can open the curtain for you!!!
