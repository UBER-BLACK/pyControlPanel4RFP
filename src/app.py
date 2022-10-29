#APP
import eel
import config
import keyboard as keyb
import serial
import time
from sys import platform
#SETUP
print("Starting...")
eel.init("web")
eel.start("main.html",mode="chrome",size=(500,500))#cmdline_args=['--start-fullscreen']#
print("work")
#MAIN
#CONTROL ARDUINO