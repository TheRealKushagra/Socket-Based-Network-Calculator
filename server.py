
import socket

from protocol import encode_message, decode_message
from netcalc import (
    subnet_calculator,
    ip_class_information,
    address_range_calculator
)

HOST = "127.0.0.1"
PORT = 5001


def process_request(request):
    """Route a request to the appropriate network calculator."""

    try:
        if not isinstance(request, dict):
            raise ValueError("Request must be a JSON object.")

        operation = request.get("operation")

        if operation == "subnet":
            result = subnet_calculator(request.get("ip", ""))

        elif operation == "ip_class":
            result = ip_class_information(request.get("ip", ""))

        elif operation == "range":
            result = address_range_calculator(request.get("cidr", ""))

        else:
            return {
                "success": False,
                "error": "Unsupported operation."
            }

        return {
            "success": True,
            "result": result
        }

    except (ValueError, TypeError) as error:
        return {
            "success": False,
            "error": str(error)
        }


def start_server():
    """Start the TCP server and process incoming client requests."""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"TCP Network Calculator Server running on {HOST}:{PORT}")
        print("Waiting for client requests...")

        while True:
            connection, address = server.accept()

            with connection:
                try:
                    print(f"\nRequest received from {address}")

                    data = b""

                    # Read one newline-delimited JSON message.
                    while b"\n" not in data:
                        chunk = connection.recv(4096)

                        if not chunk:
                            break

                        data += chunk

                    if not data:
                        continue

                    request = decode_message(data)
                    response = process_request(request)

                    connection.sendall(encode_message(response))

                    print(f"Operation: {request.get('operation')}")
                    print("Response sent successfully.")

                except (ValueError, UnicodeDecodeError) as error:
                    response = {
                        "success": False,
                        "error": f"Invalid request format: {error}"
                    }

                    connection.sendall(encode_message(response))
                    print(f"Invalid request: {error}")

                except OSError as error:
                    print(f"Connection error: {error}")


if __name__ == "__main__":
    start_server()
