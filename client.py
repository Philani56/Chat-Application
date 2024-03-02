import socket

def main():
    # Server configuration
    host = '127.0.0.1'
    port = 8888

    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to server")

    while True:
        # Get user input
        message = input("You: ")

        # Send message to server
        client_socket.sendall(message.encode())

        # Receive message from server
        data = client_socket.recv(1024).decode()
        print(f"Server: {data}")

    # Close socket
    client_socket.close()

if __name__ == "__main__":
    main()

# Reference List:
# - Python socket programming tutorial: https://realpython.com/python-sockets/