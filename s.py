# server.py 
import socket                                         
import time

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "localhost"                          

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

	
# establish a connection
clientsocket,addr = serversocket.accept()      

print("Got a connection from %s" % str(addr))

count = 0


while count < 1000:
    #send 1000 bytes
    print(count)
    out = "A" * 1000

    out = ''.join(out.split())

    clientsocket.send((out).encode('ascii'))
    count = count + 1
    time.sleep(0.01)
	
clientsocket.close()
