from socket import *

def web_client(ip_address, port, object_path):
    # IP address
    serverName = ip_address
    # Port number to use
    serverPort = port
    # Create socket for TCP
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # Connect via our socket and port number to the IP
    clientSocket.connect((serverName, serverPort))
    # Construct HTTP GET request
    http_request = f"GET {object_path} HTTP/1.1\r\n\nHost: {serverName}\r\n\r\n"
    # Send request
    clientSocket.send(http_request.encode())

    # Initialize an empty response
    response = ""
    # Loop to receive the complete response
    while True:
        # Receive part of the response
        received_data = clientSocket.recv(1024)
        # If no more data, break out of the loop
        if not received_data:
            break
        # Decode and add to the response
        response += received_data.decode()
    # Display
    print('Message from server: ', response)
    clientSocket.close()






