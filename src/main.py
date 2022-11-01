#####----------------------
##### SETUP
#####----------------------
import sys
import platform
import os
import keyboard
import random
import serial
import config
import time

key_move_forward  = config.keyboard_move_forward
key_move_left     = config.keyboard_move_left
key_move_right    = config.keyboard_move_right
key_move_back     = config.keyboard_move_back
key_reverse_roller= config.keyboard_reverse_roller
system = platform.system()
move = [0,0]

#####----------------------
##### MAIN
#####----------------------
while True:
    #                                                               MOVE
    keyboard.add_hotkey(f"{key_move_forward}",                  lambda:forward())       #HOT-KEY FORWARD
    def forward():
        move[0]=255
    keyboard.add_hotkey(f"{key_move_back}",                     lambda:back())          #HOT-KEY BACK
    def back():
        move[0]=-255
    keyboard.add_hotkey(f"{key_move_left}",                     lambda:left())          #HOT-KEY LEFT
    def left():
        move[1]=-255
    keyboard.add_hotkey(f"{key_move_right}",                    lambda:right())         #HOT-KEY RIGHT
    def right():
        move[1]=255
    keyboard.add_hotkey(f"{key_move_forward}+{key_move_left}",  lambda:forward_left())  #HOT-KEY FORWARD + LEFT
    def forward_left():
        move[0]=255
        move[1]=-255
    keyboard.add_hotkey(f"{key_move_forward}+{key_move_right}", lambda:forward_right()) #HOT-KEY FORWARD + RIGHT
    def forward_right():
        move[0]=255
        move[1]=255
    keyboard.add_hotkey(f"{key_move_back}+{key_move_left}",     lambda:back_left())     #HOT-KEY BACK + LEFT
    def back_left():
        move[0]=-255
        move[1]=-255
    keyboard.add_hotkey(f"{key_move_back}+{key_move_right}",    lambda:back_right)      #HOT-KEY BACK + RIGHT
    def back_right():
        move[0]=-255
        move[1]=255
    keyboard.add_hotkey(' ',                    lambda:print('hit'))                    #HOT-KEY HIT
    print(f"Y: {move[0]} X: {move[1]}")
    move=[0,0]
    time.sleep(0.05)