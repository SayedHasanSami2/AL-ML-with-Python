import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5001       # Port number > 1023

# Step 1: Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Bind to host and port
server_socket.bind((HOST, PORT))

# Step 3: Listen for incoming connections
server_socket.listen(1)
print(f"[ECHO SERVER] Listening on {HOST}:{PORT}...")

# Step 4: Accept client connection
conn, addr = server_socket.accept()
print(f"[ECHO SERVER] Connected by {addr}")

try:
    # Step 5: Communication loop
    while True:
        data = conn.recv(1024)
        if not data:
            print("[ECHO SERVER] No data received. Closing.")
            break

        message = data.decode().strip()
        print(f"[CLIENT]: {message}")

        if message.lower() == "exit":
            conn.send("Server: exit acknowledged. Closing connection.".encode())
            print("[ECHO SERVER] Exit received. Closing connection.")
            break

        # Step 6: Echo back message
        conn.send(f"Echo: {message}".encode())

finally:
    conn.close()
    server_socket.close()
    print("[ECHO SERVER] Server socket closed.")
