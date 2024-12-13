from socket import *
import os

# my ip 192.168.0.157

# Use this port number
serverPort = 12000
# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
# Bind our port number to the socket we created
serverSocket.bind(('', serverPort))
# Start listening (UDP doesn't do this)
serverSocket.listen(1)

# Returns the content type based on the file extension
def get_content_type(file_path):
    if file_path.endswith('.html'):
        return 'text/html'
    elif file_path.endswith('.txt'):
        return 'text/plain'
    elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
        return 'image/jpeg'
    elif file_path.endswith('.png'):
        return 'image/png'
    else:
        return 'application/octet-stream'
    
# Generate HTTP response message
def generate_http_response(status_code, status_text, content_type, content):
    response = f'HTTP/1.1 {status_code} {status_text}\r\n'
    response += 'Content-Type: ' + content_type + '\r\n'
    response += 'Content-Length: ' + str(len(content)) + '\r\n' + '\n\n'
    response += content
    return response

print('Server is ready to receive')

while True:
    # Accept connection (UDP doesn't do this)
    connectionSocket, addr = serverSocket.accept()
    # Receive and decode
    sentence = connectionSocket.recv(1024).decode()

    # Extract method and URL from the request 
    lines = sentence.split('\n')
    first_line = lines[0]
    method, path, version = first_line.split()

    # Check the method is 'Get'
    if method == 'GET':
        # Remove the leading slash 
        file_path = path[1:]

        # Check if the file exists
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file: # open file as binary and then decode to utf-8 in the response 
                content = file.read()
                content_type = get_content_type(file_path)
                response = generate_http_response('200', 'OK', content_type, content.decode('utf-8', 'ignore'))
        else:
            content = '<html><body><h1>404 Not Found</h1></body></html>'
            response = generate_http_response('404', 'Not Found', 'text/html', content)

        # Send it back
        connectionSocket.sendall(response.encode()) # use sendall instead of send to make sure all responses are sent 
    else:
        # Method not allowed
        content = '<html><body><h1>405 Method Not Allowed</h1></body></html>'
        response = generate_http_response('405', 'Method Not Allowed', 'text/html', content)
        connectionSocket.sendall(response.encode()) 

    # Close the socket
    connectionSocket.close()
