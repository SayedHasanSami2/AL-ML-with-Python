import socket

HOST = '127.0.0.1'
PORT = 5002

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print(f"[MATH CLIENT] Connected to {HOST}:{PORT}")

try:
    while True:
        expr = input("Enter '<num1> <num2> <op>' or 'exit': ")
        client_socket.send(expr.encode())

        reply = client_socket.recv(1024).decode()
        print(f"[SERVER]: {reply}")

        if expr.lower() == "exit":
            break
finally:
    client_socket.close()
