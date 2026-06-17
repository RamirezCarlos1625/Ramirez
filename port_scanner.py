import socket
import time

ALLOWED_TARGETS = {"127.0.0.1", "localhost", "scanme.nmap.org"}


def scan_port(host: str, port: int) -> None:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            status = "OPEN" if result == 0 else "CLOSED"
            print(f"Port {port}: {status}")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")


if __name__ == "__main__":
    try:
        target = input("Enter target (127.0.0.1, localhost, or scanme.nmap.org): ").strip()
        if target not in ALLOWED_TARGETS:
            raise ValueError("Only localhost or scanme.nmap.org allowed.")

        start_port = int(input("Start Port: ").strip())
        end_port = int(input("End Port: ").strip())

        if not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535):
            raise ValueError("Ports must be between 1 and 65535.")

        if start_port > end_port:
            raise ValueError("Start Port must be less than or equal to End Port.")

        print(f"\nScanning {target}...\n")
        for port in range(start_port, end_port + 1):
            scan_port(target, port)
            time.sleep(0.1)

        print("\nScan Complete")

    except ValueError as e:
        print(f"Input Error: {e}")
    except socket.gaierror:
        print("Host could not be resolved.")
    except Exception as e:
        print(f"Error: {e}")
