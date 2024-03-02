import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    while True:
        # Receive message from client
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received message from {client_address}: {data}")

        # Send message back to client
        client_socket.sendall(data.encode())

    print(f"Connection from {client_address} closed")
    client_socket.close()

def main():
    # Server configuration
    host = '127.0.0.1'
    port = 8888

    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()

        # Create a new thread to handle client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()

# Reference List:
# - Python socket programming tutorial: https://realpython.com/python-sockets/
