from PIDfunctions import PID

setpoint = float(input("Enter target temp (C): "))

controller = PID(
        setpoint=setpoint,  # Target temp in °C
        TARGET_PORT="COM4",    #desired port 
        TARGET_BAUD=5000000,
    )

controller.simulation()
