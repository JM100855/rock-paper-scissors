import socket

def play_game(player1, player2):
    # Game logic implementation
    # Compare choices, determine winner, and return the result

# Set up the server
 server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 server_host = '10.113.6.223'  # Server IP address
 server_port = 14774  # Server port number
 server_socket.bind((server_host, server_port))
 server_socket.listen(2)

 print("Waiting for players to connect...")

# Accept player connections
 player1_socket, player1_address = server_socket.accept()
 print("Player 1 connected.")

 player2_socket, player2_address = server_socket.accept()
 print("Player 2 connected.")

# Start the game
 while True:
    # Receive player choices
    player1_choice = player1_socket.recv(1024).decode().strip().lower()
    player2_choice = player2_socket.recv(1024).decode().strip().lower()

    if not player1_choice or not player2_choice:
        break

    # Play the game
    result = play_game(player1_choice, player2_choice)

    # Send the game result to players
    player1_socket.send(result.encode())
    player2_socket.send(result.encode())

# Close the connections
 player1_socket.close()
 player2_socket.close()
 server_socket.close()