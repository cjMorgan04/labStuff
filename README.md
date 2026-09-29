# labStuff
This repo contains the collected works I collected from my work in lab. I was given permission to use these for my GITHUB. 

####################
PIDfunctions/PIDmain

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

As mentioned above I used AI to code mainSPD1305X and I wanted to make this note so that those adapting the code or future employers alike, if curious, will see my perspective on my usage. Firstly, in the condensed matter that I am a part of AI is allowed and encouraged to bridge gaps in programming knowledge. My undergraduate university has given us access to the pro model of Gemini. Because of this, AI is pervasive in my daily life. However, I try to err on the side of caution specifically when it comes to a lab/professional section. AI works great when handling specific syntax. While I am familiar with Python and C++, I lack an encyclopedic knowledge of coding conventions unlike ChatGPT or Gemini as it would seem. And I can confidently say that I have become a more adept programmer by looking at AI code or ideas relative to if I had elected to self study. Inversely, AI is putting an immense strain on the natural world and early research suggests it is rotting our brains. It would be irresponsible to claim that the user is at fault, realistically, I believe the blame is more on the lack of guardrails on such a new technology. Anyway, I try to remember that my interests are a product of wanting to engineer a better world for everyone in a manner that I also can enjoy. AI can work in my favor if used in a balanced way so at least in a professional setting it would be wise to restrain its usage until its benefit is absolutely clear.        
