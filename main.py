import screen_brightness_control as sbc
import time

default = 100
blackout = 0
timeout = 5
loop_var = 0

def screen_blackout():
    sbc.set_brightness(blackout)
    time.sleep(0.01)
    sbc.set_brightness(blackout)
    time.sleep(0.01)
    sbc.set_brightness(blackout)
    time.sleep(0.01)
    sbc.set_brightness(blackout)
    time.sleep(0.01)
    sbc.set_brightness(blackout)
    time.sleep(0.01)
    sbc.set_brightness(blackout)
    time.sleep(0.01)
    sbc.set_brightness(blackout)
    time.sleep(0.01)
    sbc.set_brightness(blackout)
    time.sleep(0.01)
    sbc.set_brightness(blackout)

def blackout_screen():
    screen_blackout()
    screen_blackout()
    screen_blackout()

runtime = timeout + 1

while (loop_var < runtime):   
    blackout_screen()
    loop_var = loop_var + 1
else:
    sbc.set_brightness(default)
