import socket

# Server Configuration
HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print(f"Connected to server {HOST}:{PORT}")

while True:
    # First, send a message
    client_message = input("You: ")
    client.send(client_message.encode())

    # Then, receive a response from the server
    server_message = client.recv(1024).decode()
    if not server_message:
        break
    print(f"Server: {server_message}")

client.close()
