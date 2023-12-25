import socket
host = '0.0.0.0'
port = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(1)

print('Listening on port %s ...' % port)
while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()
    # Get the client request
    request = client_connection.recv(1024).decode()
    headers = request.split('\n')
    filename = headers[0].split()[1]

    # Get the content of the file
    if filename == '/':
        filename = './task.txt'
    if filename == '/rakib':
        filename = './task.txt'

    fin = open(filename)
    content = fin.read()
    fin.close()
    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\n' + content
    # response = 'HTTPS/3.0 404 NOT FOUND\n\nFile Not Found'

    client_connection.sendall(response.encode('utf-8'))
    client_connection.close()

# Close socket
server_socket.close()
