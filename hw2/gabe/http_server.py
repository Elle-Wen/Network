import os

def handle_request(request):
    method, files, _ = request.split('\n')[0].split()

    if method != "GET":
        response_status = "HTTP/1.1 405 Method Not Allowed\r\n"
        response_headers = "Allowed: GET\r\nContent-length : 0\r\n\n"
        response_body = ""
    else:
        print(files)
        if os.path.exists(files):
            with open(files, 'r') as file:
                content = file.read()
            response_status = "HTTP/1.1 200 OK\r\n"
            response_body = content
        else:
            response_status = "HTTP/1.1 404 Not Found\r\n"
            response_body = "404 Not Found"

        response_headers = "Server: Gabe's local server\r\nContent-Length: {}\r\n\n".format(len(response_body))
    response = response_status + response_headers + response_body
    return response.encode()
