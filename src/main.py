#####----------------------
##### SETUP
#####----------------------
import sys
import platform
import os
import keyboard
import serial
import config
import time


system = platform.system()


key_move_forward    = config.keyboard_move_forward
key_move_left       = config.keyboard_move_left
key_move_right      = config.keyboard_move_right
key_move_back       = config.keyboard_move_back

key_hit             = config.keyboard_hit
key_reverse_roller  = config.keyboard_reverse_roller


bt_port             = config.bluetooth_port
bt_mac              = config.bluetooth_mac


set_keyboard_work   = config.settings_keyboard_work
set_hit_power       = config.settings_hit_power
set_roller_power    = config.settings_roller_power
#####----------------------
##### MAIN
#####----------------------
if system == "Linux":
    os.system("sudo rfcomm unbind 0")
    time.sleep(1)
    os.system(f"sudo rfcomm bind 0 {bt_mac}")
    bluetooth = serial.Serial("/dev/rfcomm0", 115200)
    bluetooth.reset_input_buffer()
while True:
    move_y              = 0
    move_x              = 0
    hit                 = 0
    roller              = set_roller_power
    if keyboard.is_pressed(f"ctrl + esc"):               #KEY-STOP
        print("STOP")
        bluetooth.close()
        sys.exit()
    if set_keyboard_work == True:                                     #KEYBOARD
        #MOVE
        if keyboard.is_pressed(f"{key_move_forward}"):      #KEY-FORWARD
            move_y= 255
        elif keyboard.is_pressed(f"{key_move_back}"):       #KEY-BACK
            move_y=-255
        if keyboard.is_pressed(f"{key_move_left}"):         #KEY-LEFT
            move_x=-255
        elif keyboard.is_pressed(f"{key_move_right}"):      #KEY-RIGHT
            move_x= 255
        #HIT
        if keyboard.is_pressed(f"{key_hit}"):               #KEY-HIT
            hit=set_hit_power
            roller=-255
        elif keyboard.is_pressed(f"{key_reverse_roller}"):  #KEY-REVERSE ROLLER
            roller=-255
    
    time.sleep(0.05)