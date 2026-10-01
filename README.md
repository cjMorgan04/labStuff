# labStuff
This repo contains software developed for my lab. The projects are focused on control and automation of experiments. I was given permission to publish these to my GITHUB. 

####################
PIDfunctions/PIDmain ~ In Development

This code is designed to alter the output power in steps to reach a set power via a proportional–integral–derivative (PID) controller. This is designed to be the culmination of all of the code placed underneath this. I opted to write the controller as a class because the main function will likely be expanded. As of writing this the core logic has been completed but actually sending these commands to the DC power supply still must be implemented.


########
SPD1305X

Features basic functions that the Siglent 1305X programmable DC power supply comes with. 

############
mainSPD1305X

Designed to observe the graphical behavior of a power vs temperature curve for an aluminum block. This is designed to slowly ramp up the power provided to the aluminum cube. Temperature measured by a thermocouple, read via a serial monitor. 

##################
max31855/main31855

Driver and display code for the max 31855 thermocouple for a microcontroller. This is programmed in micropython specifically for a pico 2. 

#############
serialMonitor

Reads and displays output from separate ports. Was created so that the pico 2 may run its temperature code independently of mainSPD1305X.

#######
picoLCD

Driver file for the Waveshare pico lcd 1.8 inch display. 



###################
Personal Note on AI

As mentioned above I used AI to code mainSPD1305X. I generally try to avoid using AI unless it is for learning coding conventions or syntax. This use was disclosed to and approved by the relevant lab members/leadership.
