import socket

HOST = '127.0.0.1'
PORT = 5001

# Step 1: Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to server
client_socket.connect((HOST, PORT))
print(f"[ECHO CLIENT] Connected to {HOST}:{PORT}")

try:
    # Step 3: Communication loop
    while True:
        msg = input("You: ")
        client_socket.send(msg.encode())

        reply = client_socket.recv(1024).decode()
        print(f"[SERVER]: {reply}")

        if msg.lower() == "exit":
            print("[ECHO CLIENT] Exit sent. Closing client.")
            break
finally:
    client_socket.close()
