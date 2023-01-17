import socket

# socket is a very low level API
# 1. Create socket object
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# AF_INET -> ipv4
# SOCK_STREAM -> TCP

server_host = '127.0.0.1'
server_port = 4440
# 2. connect to server via 3 way handshake
client_sock.connect((server_host, server_port))

# 3. Send data
client_sock.sendall(bytes('Hello from client'.encode('utf-8')))

# how will we send 1 GB across the internet? WE will break it into parts and then send
# send(We will need to manually do the breaking of the data into smaller chunks) vs
# sendall (Just pass the data, it will internally chop it up into small pieces)

# 4. Receive response from server
response_data = client_sock.recv(1024)

print(response_data)

# 5. close the connection
client_sock.close()

