# UDP Server

# How Python makes it easy to make sockets
from socket import *
import random
def start_server(drop_rate):
    # drop_rate: The percentage (0-100) of packets to randomly drop.
    # serverName here works as the IP address
    # serverPort is on what port we will open up our connection
    serverPort = 12000
    # SOCK_STREAM for TCP, SOCK_DGRAM for UDP
    # This gets Python to create our socket
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    # "bind" in this case assigns the port number to our socket 
    serverSocket.bind(('', serverPort))
    # Print message just to check everything happened correctly
    print ("Server is ready to receive")
    # Loop to be continuously listening
    while True:
        # We receive, both, message and clientAddress and use 2048 buffer
        message, clientAddress = serverSocket.recvfrom(2048)
        if random.randint(1,100) > drop_rate: # not dropping the package, otherwise drop
        # Modify the message as "proof" we got it at the server, note use of decode()
            modifiedMessage = message.decode().upper()
            # Send the message back, note the use of encode()
            serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        else:
            print("some data is dropped")
