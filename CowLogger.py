import gpiozero
from signal import pause
import time

button = gpiozero.Button(2)

def h2o_low():
    cow_log = open("CowLog.txt", "a+")
    cow_log.write("Water Low (Circ Opn)" + time.ctime() + " \n")
    print("LOG: H2O LOW")
    cow_log.close()
    
def h2o_normal():
    cow_log = open("CowLog.txt", "a+")
    cow_log.write("Water Normal (Circ Cls) " + time.ctime() + " \n")
    print("LOG: H2O NORMAL")
    cow_log.close()
    
button.when_released = h2o_low

button.when_pressed = h2o_normal

pause()