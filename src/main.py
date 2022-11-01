#####----------------------
##### SETUP
#####----------------------
import sys
import os
import keyboard
import random
import serial
import config


keyboard_move_forward  = config.keyboard_move_forward
keyboard_move_left     = config.keyboard_move_left
keyboard_move_right    = config.keyboard_move_right
keyboard_move_back     = config.keyboard_move_back
keyboard_reverse_roller= config.keyboard_reverse_roller
#####----------------------
##### MAIN
#####----------------------
#   MOVE
keyboard.add_hotkey(keyboard_move_forward, lambda:wasd(255,0)) #forward
keyboard.add_hotkey(keyboard_move_left, lambda:wasd(0,-255)) #left
keyboard.add_hotkey(keyboard_move_right, lambda:wasd(0,255)) #right
keyboard.add_hotkey(keyboard_move_back, lambda:wasd(-255,0)) #back


keyboard.add_hotkey(f"{keyboard_move_forward} + {keyboard_move_right}", lambda:wasd(255,255)) #forward+right


def wasd(Y,X):
    print(Y,X)
keyboard.wait()