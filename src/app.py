#APP
import eel
import config
from sys import platform
#SETUP
print("Starting...")
eel.init("web")
eel.start("error_osnotupported.html",mode="chromium", port="",size=(100,100)) #cmdline_args=['--start-fullscreen']

#MAIN