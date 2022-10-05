import numpy as np 
import pandas as pd
import read_write as motor_cntrl 
import time 
import random
import os
if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

DELAY_BETWEEN_FRAMES = 0.3
# Mapping procces between 0-1023
def multiplied(dfm): 
    result_of_mapping = dfm/0.297
    result_of_rounded_number = round(result_of_mapping)
    return result_of_rounded_number

# Read csv file
# df = pd.read_csv('/home/berkay/Masaüstü/DynamixelSDK/tests/protocol1_0/anglesofmotors.csv')
#print(df)

# Convert data frame to matrix 
# dfm = np.array(df)

# Initial Position of the motors                                                                                                                   
goal = [ 512 ,380, 680 ]
index = 0

while 1:
    for i in range(2,5):
        motor_cntrl.SDK(i,goal[index])
        time.sleep(2)
        index = index + 1
        if i == 5:
            for j in range(2,5):
                goal[j] = random.uniform(500,690)
            i = 2
            index = 0    


#Algorithm of the walking
# for frame in range(0,51,1): # Each frame are in loop (we can change of the range value that we can need it)
#    for motor_id in range(1,13): # This is respect to motor id declaration 
#        motor_cntrl.SDK(motor_id, present[motor_id], multiplied(dfm[frame][motor_id+1])+present[motor_id])
    
#    time.sleep(DELAY_BETWEEN_FRAMES) # Delay for frames