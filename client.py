import socket

# Set up the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = '10.113.6.223'  # Replace with the server's IP address
server_port = 14774  # Replace with the server's port number

# Connect to the server
client_socket.connect((server_host, server_port))

# Get player choice
choice = input("Enter your choice (rock/paper/scissors): ")

# Send the choice to the server
client_socket.send(choice.encode())

# Receive and print the game result
result = client_socket.recv(1024).decode()
print(result)

# Close the connection
client_socket.close()