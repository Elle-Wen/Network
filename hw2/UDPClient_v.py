# UDP Client

# How Python makes it easy to make sockets
from socket import *
import time
# serverName here works as the IP address
# serverPort is on what port we will open up our connection
serverName = '192.168.0.157'
serverPort = 12000
total_rtt = 0
received_pings = 0

# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
# This gets Python to create our socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1) # set 1 sec timeout for response

for sequence_number in range(0,10):
    try: 
        message = f'ping {sequence_number}'
        # Use socket to send message, note the use of encode() and the address
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        start_time = time.time() # send ping and record the time
        # Receiving follows similar format, 2048 is buffer size for input
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        end_time = time.time() # wait for response and record the time
        rtt = end_time - start_time
        print(modifiedMessage.decode(), "rtt: ", rtt)

        
        total_rtt += rtt 
        received_pings += 1

    except timeout: # not received by the server
        print(f"Ping {sequence_number}", "rtt:  *")
#calculate stats
packet_loss_rate = ((10 - received_pings) / 10) * 100
average_rtt = total_rtt / received_pings if received_pings > 0 else float('inf')
print("\n--- Ping statistics ---")
print(f"10 packets transmitted, {received_pings} packets received, {packet_loss_rate:.2f}% packet loss")
print(f"Average RTT: {average_rtt:.4f}s")

clientSocket.close()



