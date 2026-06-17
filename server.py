import socket

HOST = "127.0.0.1"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = server.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        if not data:
            print("No data received.")
        else:
            message = data.decode("utf-8")
            print(f"Client: {message}")
            conn.sendall(f"Server received: {message}".encode("utf-8"))
        print("Connection closed.")
