import socket

HOST = '0.0.0.0'
PORT = 5002

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"[MATH SERVER] Listening on {HOST}:{PORT}...")

conn, addr = server_socket.accept()
print(f"[MATH SERVER] Connected by {addr}")

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break

        text = data.decode().strip()
        print(f"[CLIENT]: {text}")

        if text.lower() == "exit":
            conn.send("Server: exit acknowledged. Closing connection.".encode())
            break

        # Expected format: num1 num2 operator
        parts = text.split()
        if len(parts) != 3:
            conn.send("Error: use format '<num1> <num2> <op>' e.g. '12 4 +'".encode())
            continue

        a_str, b_str, op = parts

        # Convert to float
        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            conn.send("Error: numbers must be valid numeric values.".encode())
            continue

        # Perform operation
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                conn.send("Error: Division by zero.".encode())
                continue
            result = a / b
        else:
            conn.send("Error: Unsupported operator. Use + - * /".encode())
            continue

        conn.send(f"Result: {result}".encode())

finally:
    conn.close()
    server_socket.close()
    print("[MATH SERVER] Server socket closed.")
