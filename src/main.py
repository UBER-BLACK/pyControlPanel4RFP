#####----------------------
##### SETUP
#####----------------------
import sys, platform, os, keyboard, serial, config, time


system              = platform.system()
key_move_forward    = config.keyboard_move_forward
key_move_left       = config.keyboard_move_left
key_move_right      = config.keyboard_move_right
key_move_back       = config.keyboard_move_back
key_hit             = config.keyboard_hit
key_reverse_roller  = config.keyboard_reverse_roller
bt_speed            = config.bluetooth_speed
bt_port             = config.bluetooth_port
bt_mac              = config.bluetooth_mac
set_hit_stretch     = config.settings_hit_stretch
set_hit_power       = config.settings_hit_power
set_roller_power    = config.settings_roller_power
#####----------------------
##### MAIN
#####----------------------
if system == "Linux":
    os.system(f"rfcomm bind 0 {bt_mac}")
    time.sleep(1)
    bluetooth = serial.Serial("/dev/rfcomm0",bt_speed)
    bluetooth.close
    bluetooth.open
    bluetooth.reset_input_buffer()
else:
    print(f"You OS ({system}) is not support")
    sys.exit()
def keyboard_data():
    move_y      = 0
    move_x      = 0
    hit_x       = set_hit_stretch
    roller_x    = set_roller_power
    #MOVE
    if keyboard.is_pressed(f"{key_move_forward}"):      move_y= 255
    elif keyboard.is_pressed(f"{key_move_back}"):       move_y=-255
    if keyboard.is_pressed(f"{key_move_left}"):         move_x=-255
    elif keyboard.is_pressed(f"{key_move_right}"):      move_x= 255
    #HIT
    if keyboard.is_pressed(f"{key_hit}"):               hit_x=set_hit_power
    elif keyboard.is_pressed(f"{key_reverse_roller}"):  roller_x=-255
    time.sleep(0.05)
    return(move_y,move_x,hit_x,roller_x)

while True:
    if keyboard.is_pressed(f"ctrl + 1"):               #KEY-STOP
        print("STOP")
        bluetooth.close()
        os.system("rfcomm unbind 0")
        sys.exit()
    send_data = f"{keyboard_data()}\n"
    bluetooth.open
    bluetooth.write(send_data.encode())
    bluetooth.close
    time.sleep(0.05)
