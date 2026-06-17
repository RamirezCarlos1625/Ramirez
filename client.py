import socket

HOST = "127.0.0.1"
PORT = 9999

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("Connected to server.")

        message = input("Enter message: ").strip()
        if not message:
            raise ValueError("Message cannot be empty.")

        client.sendall(message.encode("utf-8"))
        response = client.recv(1024).decode("utf-8")
        print(f"Server Response: {response}")

    print("Disconnected.")

except ConnectionRefusedError:
    print("Error: Server is not running.")

except ValueError as e:
    print(f"Input Error: {e}")

except Exception as e:
    print(f"Error: {e}")
