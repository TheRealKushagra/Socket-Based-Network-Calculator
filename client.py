import socket

from protocol import encode_message, decode_message

HOST = "127.0.0.1"
PORT = 5001


def send_request(request):
    """Send a request to the TCP server and return its response."""

    try:
        with socket.create_connection((HOST, PORT), timeout=5) as client:
            client.sendall(encode_message(request))

            data = b""

            while b"\n" not in data:
                chunk = client.recv(4096)

                if not chunk:
                    break

                data += chunk

            if not data:
                return {
                    "success": False,
                    "error": "The server closed the connection without a response."
                }

            return decode_message(data)

    except (ConnectionRefusedError, TimeoutError, OSError) as error:
        return {
            "success": False,
            "error": f"Could not communicate with the server: {error}"
        }

    except (ValueError, UnicodeDecodeError) as error:
        return {
            "success": False,
            "error": f"Invalid response received from the server: {error}"
        }


def main():
    print("\n===== Network Calculator Client =====")
    print("1. Subnet Calculator")
    print("2. IPv4 Class Detector")
    print("3. IP Address Range Calculator")

    choice = input("\nChoose an operation (1-3): ").strip()
    value = input("Enter an IP address or CIDR: ").strip()

    if choice == "1":
        request = {"operation": "subnet", "ip": value}
    elif choice == "2":
        request = {"operation": "ip_class", "ip": value}
    elif choice == "3":
        request = {"operation": "range", "cidr": value}
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        return

    response = send_request(request)

    if response.get("success"):
        print("\n===== Result =====")

        for key, result in response["result"].items():
            print(f"{key}: {result}")
    else:
        print("\nError:", response.get("error", "Unknown error"))


if __name__ == "__main__":
    main()