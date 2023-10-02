import socket

def get_server_ip():
    # Create a temporary socket
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    temp_socket.connect(("8.8.8.8", 80))
    server_ip = temp_socket.getsockname()[0]
    temp_socket.close()
    return server_ip

def get_server_port():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 0))
    server_port = server_socket.getsockname()[1]
    server_socket.close()
    return server_port

# Get the server IP address and port
server_ip = get_server_ip()
server_port = get_server_port()

print(f"Server IP Address: {server_ip}")
print(f"Server Port Number: {server_port}")