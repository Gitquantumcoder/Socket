import socket
import threading
import os

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP address and port number
HOST = "127.0.0.1"
PORT = 5000

# Create a folder for client logs
os.makedirs("logs", exist_ok=True)

# Bind the socket to the IP address and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen(5)

print("Server is waiting for connections...")


# Function to handle one client
def handle_client(client_socket, client_address):

    # Create a separate log file for this client
    client_ip = client_address[0].replace(".", "_")
    client_port = client_address[1]
    log_file = f"logs/client_{client_ip}_{client_port}.txt"

    print("Client connected:", client_address)

    with open(log_file, "a") as file:
        file.write("Client connected: " + str(client_address) + "\n")

        # Keep communicating until the client exits
        while True:

            # Receive message from the client
            message = client_socket.recv(1024).decode()

            # If the client closes the connection
            if not message:
                break

            print("Client", client_address, ":", message)

            # Store the message in the client's log file
            file.write("Client: " + message + "\n")

            # Check whether the client wants to exit
            if message.lower() == "exit":
                reply = "Connection closed. Goodbye!"
                client_socket.send(reply.encode())
                file.write("Server: " + reply + "\n")
                break

            # Send a reply to the client
            reply = "Message received by the server!"
            client_socket.send(reply.encode())

            # Store the server reply in the log file
            file.write("Server: " + reply + "\n")

    # Close this client's connection
    client_socket.close()

    print("Client disconnected:", client_address)


# Accept many clients
while True:

    # Accept a new client connection
    client_socket, client_address = server_socket.accept()

    # Create a separate thread for the client
    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address)
    )

    # Start the client thread
    client_thread.start()
