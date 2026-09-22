import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP address and port number
HOST = "127.0.0.1"
PORT = 5000

# Bind the socket to the IP address and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen(1)

print("Server is waiting for connection...")

# Accept a connection from the client
client_socket, client_address = server_socket.accept()

print("Client connected:", client_address)

# Receive message from the client
message = client_socket.recv(1024).decode()

print("Message from client:", message)

# Send a reply to the client
reply = "Message received by the server!"
client_socket.send(reply.encode())

# Close the connection
client_socket.close()
server_socket.close()

print("Connection closed.")