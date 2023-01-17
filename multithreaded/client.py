import socket
import threading
import requests

# socket is a very low level API

# AF_INET -> ipv4
# SOCK_STREAM -> TCP

server_host = '127.0.0.1'
server_port = 4440

def fetch_data_from_server(i):
    # 1. Create socket object
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. connect to server via 3 way handshake
    client_sock.connect((server_host, server_port))

    # 3. Send data
    client_sock.sendall(bytes('Hello from client {}'.format(i).encode('utf-8')))

    # 4. Receive response from server
    response_data = client_sock.recv(1024)

    print(response_data)

    # 5. close the connection
    client_sock.close()

for i in range(100):
    t = threading.Thread(target=fetch_data_from_server, args=(i,))
    t.start()
