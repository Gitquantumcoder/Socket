import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server IP address and port number
HOST = "127.0.0.1"
PORT = 5000

# Connect to the server
client_socket.connect((HOST, PORT))

print("Connected to the server.")

# Take a message from the user
message = input("Enter message: ")

# Send the message to the server
client_socket.send(message.encode())

# Receive reply from the server
reply = client_socket.recv(1024).decode()

print("Server:", reply)

# Close the connection
client_socket.close()