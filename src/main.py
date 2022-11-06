#####----------------------
##### SETUP
#####----------------------
import sys, platform, os, keyboard, serial, config, time 
if platform.system() == "Linux":
    print("OS is support")
else:
    print("OS is not support")
    sys.exit()   
#####----------------------
##### MAIN
#####----------------------
def debug(state,command,text):
    work    = config.settings_debug_mode
    cli_mode= config.settings_cli_mode
    if (work==True) and (cli_mode==False):
        print(f"[{state}] {command}: {text}")
        return(True)
    else:
        return(False)
def keyboard_data():
    #   BIND KEYS
    key_move_forward    = config.keyboard_move_forward
    key_move_left       = config.keyboard_move_left
    key_move_right      = config.keyboard_move_right
    key_move_back       = config.keyboard_move_back
    key_hit             = config.keyboard_hit
    key_reverse_roller  = config.keyboard_reverse_roller
    #   SETTINGS
    move_y              = config.settings_move_y_balance
    move_x              = config.settings_move_x_balance
    hit_x               = config.settings_hit_stretch
    rev_roller_x        = config.settings_roller_power
    hit_power           = config.settings_hit_power
    #                   ENGINE CONTROL
    if keyboard.is_pressed(f"{key_move_forward}"):      move_y= 255         #FORWARD
    elif keyboard.is_pressed(f"{key_move_back}"):       move_y=-255         #BACK
    if keyboard.is_pressed(f"{key_move_left}"):         move_x=-255         #LEFT
    elif keyboard.is_pressed(f"{key_move_right}"):      move_x= 255         #RIGHT
    #                   WEAPON CONTROL
    if keyboard.is_pressed(f"{key_hit}"):               hit_x=hit_power     #HIT
    elif keyboard.is_pressed(f"{key_reverse_roller}"):  rev_roller_x=-255   #REV-ROLLER
    time.sleep(0.02)
    int_keyboard_data = move_y,move_x,hit_x,rev_roller_x
    debug(True,"Keyboard_data",int_keyboard_data)
    return(int_keyboard_data)
def bluetooth_connect():
    system      = platform.system()
    bt_speed    = config.bluetooth_speed
    bt_port     = config.bluetooth_port
    bt_mac      = config.bluetooth_mac
    if system == "Linux":
        os.system(f"rfcomm bind 0 {bt_mac}")
        time.sleep(1)
        global bluetooth
        bluetooth = serial.Serial("/dev/rfcomm0",bt_speed)
        bluetooth.close
        bluetooth.open
        bluetooth.reset_input_buffer()
        time.sleep(2)
        debug(True,"bluetooth","Connect")
        return(True)
    else:
        debug(False,"bluetooth","Connect")
        return(False)
def bluetooth_disconnect():
    system      = platform.system()
    bt_speed    = config.bluetooth_speed
    bt_port     = config.bluetooth_port
    bt_mac      = config.bluetooth_mac
    if system == "Linux":
        bluetooth.close()
        os.system("rfcomm unbind 0")
        time.sleep(2)
        debug(True,"bluetooth","Disconect")
        return(True)
    else:
        debug(False,"bluetooth","Disconect")
        return(False)
def bluetooth_senddata(send_data):
    pass
    debug(True,"bluetooth","Send")
def mini_subsustem(): 
    if keyboard.is_pressed(f"ctrl + q"):               
        print("EXIT")
        sys.exit()
    elif keyboard.is_pressed(f"alt"):
        print("RECONNECT")
        bluetooth_disconnect()
        bluetooth_connect()  
bluetooth_connect() #AUTO-CONNECT
while True:
    mini_subsustem()
    bluetooth_senddata(keyboard_data())