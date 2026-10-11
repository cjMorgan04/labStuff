import time
from serialMonitor import read_serial_string
from SPD1305X import VisaClose, VisaConnect, VisaQuery, VisaWrite


class PID:                                                                                      #Windows port syntax                                        
    def __init__(
        self,
        setpoint=0.0, #Target temp in C
        pv=0.0,   #Current Temperature in C
        kp=2.0, # proportional term, responds to voltage error, speeds up system response time
        ki=0.1, # intergral term, intergrates past error, gets rid of error caused by kp 
        kd=0.05, # derivative term, predicts future error, limits speed of response to prevent overshoot
        previous_error=0,
        integral=0,
        dt=1.0,  # Default to 1 second time step
        USB_RESOURCE="",
        TARGET_PORT="COM4",
        TARGET_BAUD=5000000,
    ):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.pv = pv
        self.previous_error = previous_error
        self.integral = integral
        self.dt = dt
        self.inst = VisaConnect(USB_RESOURCE)
        self.port = TARGET_PORT
        self.baudrate = TARGET_BAUD
        self.maxVoltage = 5.0
        self.maxCurrent = 1


    def pid_controller(self): #Core logic of the PID loop
        self.error = self.setpoint - self.pv
        self.integral += self.error * self.dt

        # Prevents integral term from accumulating values that freeze the voltage output at 5.0V
        max_integral = self.maxVoltage / self.ki if self.ki > 0 else 0.0
        self.integral = max(-max_integral, min(max_integral, self.integral))

        # Avoid ZeroDivisionError if dt is 0
        if self.dt > 0:
            self.derivative = (self.error - self.previous_error) / self.dt
        else:
            self.derivative = 0

        control = self.kp * self.error + self.ki * self.integral + self.kd * self.derivative

        #Update state for the next loop iteration
        self.previous_error = self.error

        

        #I decided to control the temperature with the voltage instead of the power to simplify the code 
        control = max(0.0, min(self.maxVoltage, control)) #Ensures the voltage never goes above 30V or below 0V

               #volts    
        return control

    def simulation(self):
        safe = True
        print("Starting Run... Press Ctl+C to exit")
        VisaWrite(self.inst, "OUTP CH1,ON")
        VisaWrite(self.inst, f"CH1:CURR {self.maxCurrent:.2f}")  # Set current limit to a safe value
        
        try:
            while safe: 
                # Query live values
                raw_temp = read_serial_string(self.port, self.baudrate)                   
                
        
                try:
                    # Take the Celsius reading before the comma
                    celsius_part = raw_temp.split(",")[0]  # "Temperature: 23.5C"

                    #Split on the colon and grab the right side
                    value_str = celsius_part.split(":")[-1]  # " 23.5C"

                    # Clean remaining units and whitespace
                    clean_num = value_str.replace("C", "").strip()  # "23.5"
                    self.pv = float(clean_num)  # 23.5

                except (ValueError, IndexError, AttributeError):
                    # If serial returns an error string or corrupted data, retain the last valid temperature reading
                    pass

                if self.pv <= 0.0:
                    print("SAFETY TRIP: Invalid temperature reading. Zeroing output voltage!")
                    VisaWrite(self.inst, "CH1:VOLT 0.00")
                    time.sleep(self.dt)
                    safe = False 
                    continue  # Skip PID calculation for this iteration
                

                control = self.pid_controller()
               
                VisaWrite(self.inst, f"CH1:VOLT {control:.2f}") #adjust the voltage
                print(f"Temp: {self.pv}C | Setpoint: {self.setpoint}C | Output: {control:.2f}V")

                time.sleep(self.dt)
            

                #print(f"{raw_temp}")    
           
        except KeyboardInterrupt:
            print("\n\nRun Stopped By User")

        finally:
            userChoice = input("Set new temp (Y/N)")
            if userChoice.strip().upper() == "Y": #the .upper() function converts lower case to upper case
                new_temp = float(input("Enter new target temperature: "))
                self.setpoint = new_temp
                self.simulation()  # Restart the loop with the new target
            else:
                print("Safely shutting down: Zeroing current and turning OFF output...")
                VisaWrite(self.inst, "CH1:CURR 0.000")
                VisaWrite(self.inst, "OUTP CH1,OFF")
                VisaClose(self.inst)


    
        


