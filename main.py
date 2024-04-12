import pyMeow as pm
import keyboard
import time


proc = pm.open_process("left4dead2.exe")

class Modules:
    client = pm.get_module(proc,"client.dll")["base"]

class Addresses:
    is_onground = Modules.client+0x77FBB4
    jump_input = Modules.client + 0x757DF0
    duck_input = Modules.client+0x757DA8

class Offsets:
    health = 0xEC

class Pointers:
    player = Modules.client + 0x724B58

def jump():
    pm.w_int(proc,Addresses.jump_input,5)
    time.sleep(0.01)
    pm.w_int(proc,Addresses.jump_input,4)

ply = pm.r_uint(proc,Pointers.player)      
jump()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
while True:
    time.sleep(0.008)
    if pm.r_bool(proc,Addresses.is_onground):     
        if keyboard.is_pressed("space"):
            jump()

                                          