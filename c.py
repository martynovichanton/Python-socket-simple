# client.py  
import socket
import time

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "localhost"

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
count = 0

while count < 1000:
    tm = s.recv(1000)                    
    print("%s" % tm.decode('ascii'))
    count = count + 1
    time.sleep(0.01)

s.close()