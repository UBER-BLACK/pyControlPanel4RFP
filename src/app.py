#APP
import eel
import config
from sys import platform
#SETUP
print("Starting...")
eel.init("web")
eel.start("error_osnotsupported.html",mode="chrome",size=(500,500), cmdline_args=['--start-fullscreen'])
#MAIN