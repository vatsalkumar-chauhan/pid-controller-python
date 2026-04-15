'''
PROJECT : PID Controller — DC Motor Speed Control
BY  : Vatsalkumar Chauhan
'''


# (1) I have used extra toolboxes for numerical arrays and graphs 


import numpy             
import matplotlib.pyplot as pyp 


# (2) Used constsnts


TARGET_SPEED = 100.0            # Our target rpm or speed of motor
TIME_END     = 10.0             # SImulation run time
DT           = 0.01             # time step to calculate at every 0.01 seconds 

KP           = 2                # (PID GAINS) KP = Proportional, that push to reach the target
KI           = 0.8              # KI = Integral, fixes the remaining error
KD           = 0.3              # KD = Derivative, manage the target approaching speed if we are too fast
FRICTION     = 0.1              # Work as real world resistance


#  (3) Main brain, user define function


def pid_brain():

    time             = numpy.arange(0, TIME_END, DT)       # To creates a list of numbers from 0 to 10, stepped by 0.01
    speed  = []                                            # Empty list to store motor speed at every time step


 #  (4) Starting condition, when motor is OFF


    starting_speed   = 0.0                                 # motor starts at 0 RPM
    integral         = 0.0                                 # integral memory starts at 0
    prev_error       = 0.0                                 # last error for derivative calculation


 #  (5) For loop to repeats a code several time, for every time steps


    for _ in time:


        error = TARGET_SPEED - starting_speed                        # Error is diffrence between target and present speed (P PART)

        integral = integral + (error * DT)                           # Accumulating all past errors, look for remaining errors (I PART)

        derivative = (error - prev_error) / DT                       # Look at error changing rate (D PART)

        
        output = (KP * error) + (KI * integral) + (KD * derivative)  # PID OUTPUT 
        #          P part          I part            D part

       
        
        starting_speed = starting_speed + (output * DT * 0.5) - FRICTION  # Speed changes with output, here 0.5 is scaling factor depend on motor specification in real world

        speed.append(starting_speed)                                      # TO add new value in list 
        
        prev_error = error                                                # Defining current error is equal to previous error, for claculation of D


    return time, speed


#  (6) To draw graph 

def plot_graph(time, speed):
 
    pyp.figure(figsize=(12, 7))                                                    # To create blank canvas of 12x07

    pyp.plot(time, speed, color='blue', linewidth=5, label='Motor Speed (RPM)')    # Motor speed line 

    pyp.axhline(y=TARGET_SPEED, color='orange', linestyle='--',
                linewidth=1.5, label=f'Target Speed (100 RPM)')                    # Target speed line 

   
    pyp.title('PID Controller — DC Motor Speed Control Simulation')                # TO add title
    pyp.xlabel('Time (seconds)')                                                   # To add label for x-axis
    pyp.ylabel('Speed (RPM)')                                                      # To add label for y-axis
    pyp.legend()                                                                   # Key box
    pyp.grid()                                                                     # To adds grid lines

    pyp.savefig("pid_response.png")                                                # This save the file 
    pyp.show()                                                                     # Shows a saved file
    print("Graph saved as pid_response.png")


if __name__ == "__main__":                             # Make sure code runs only when executed directly 
  time, speed = pid_brain()                            # Call PID brain to simulate and get time & speed data
  plot_graph(time, speed)                              # Give data to plot function and display the graph