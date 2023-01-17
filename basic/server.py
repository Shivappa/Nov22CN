import socket

#1. Create socket object
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_host = '127.0.0.1'
server_port = 4440
#2. Bind to host and port
server_sock.bind((server_host, server_port))

#3. Server starts listening
server_sock.listen()

#4. Accpet the connection
connection, address = server_sock.accept()

#5. Receive data
request_data = connection.recv(1024)

print(request_data)

#6. Process the data

#7. Send response back to client
connection.send(bytes('Hello from server!'.encode('utf-8')))

#8. Close the connection
connection.close()

#9. Close the socket
server_sock.close()
