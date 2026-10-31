# Socket-Based Network Calculator Service

A Python-based network calculator that provides subnet calculations, IPv4 class detection, and IP address range information through a web interface. The application uses Flask for the frontend integration and TCP sockets for communication between a client and a separate server.

## Features

- **Subnet Calculator:** Calculates the network address, subnet mask, broadcast address, prefix length, total addresses, and usable host range.
- **IPv4 Class Detector:** Identifies the IPv4 address class, default subnet mask, and address type.
- **IP Address Range Calculator:** Displays the network range, broadcast address, total addresses, and usable host range.
- **TCP Client-Server Communication:** Exchanges requests and responses using TCP sockets.
- **JSON Messaging:** Encodes requests and responses as newline-delimited JSON messages.
- **Web Interface:** Provides an interactive browser-based interface using Flask, HTML, and CSS.
- **Error Handling:** Reports invalid input and communication errors.

## Technologies Used

- Python
- Flask
- TCP sockets
- JSON
- HTML5
- CSS3
- Python `ipaddress` module

## System Architecture

The application follows this communication flow:

```text
User
 |
 v
Web Browser (index.html)
 |
 v
Flask Application (app.py)
 |
 v
TCP Client (client.py)
 |
 | TCP Socket Communication
 v
TCP Server (server.py)
 |
 v
Network Calculation Module (netcalc.py)
 |
 v
JSON Response
 |
 v
Flask Web Interface
```

The Flask application receives user input from the browser and passes the request to the TCP client. The client communicates with the TCP server, which invokes the appropriate calculation function. The result is returned to the browser and displayed to the user.

## Project Structure

```text
Socket Network Calculator/
├── app.py
├── client.py
├── server.py
├── netcalc.py
├── protocol.py
├── README.md
├── templates/
│   └── index.html
└── tests/
    └── test_netcalc.py
```

The `tests/` directory will contain automated tests once they have been created.

### Module Responsibilities

| File | Responsibility |
|---|---|
| `app.py` | Handles web routes, form submissions, and result rendering. |
| `client.py` | Sends requests to the TCP server and receives responses. |
| `server.py` | Accepts TCP connections and routes requests to calculation functions. |
| `netcalc.py` | Implements subnet, IP class, and address range calculations. |
| `protocol.py` | Encodes and decodes newline-delimited JSON messages. |
| `templates/index.html` | Defines the browser interface. |

## Requirements

- Python 3.10 or later recommended.
- Flask installed in the Python environment.
- A web browser.
- The project files in the same project directory, with `index.html` inside the `templates/` folder.

## Installation

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Install Flask:

   ```bash
   python -m pip install flask
   ```

4. Ensure that all project files are in their correct locations.

The calculation functions use Python's built-in `ipaddress` module.

## Running the Application

The TCP server and Flask application must run separately.

### Terminal 1: Start the TCP Server

```bash
python server.py
```

The server listens on `127.0.0.1:5001`.

### Terminal 2: Start the Flask Application

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

Enter an IP address or CIDR prefix into the relevant calculator and submit the form.

Keep both processes running while using the application.

## Example Inputs

| Feature | Example Input | Expected Result |
|---|---|---|
| Subnet Calculator | `192.168.1.10/24` | Network address `192.168.1.0`; broadcast address `192.168.1.255`. |
| IPv4 Class Detector | `10.0.0.1` | Class A; private address. |
| IP Address Range Calculator | `192.168.1.0/28` | Network address `192.168.1.0`; broadcast address `192.168.1.15`; 16 total addresses. |

Actual outputs depend on the input provided.

## Communication Protocol

The TCP client and server exchange newline-delimited JSON messages.

Example request:

```json
{
  "operation": "subnet",
  "ip": "192.168.1.10/24"
}
```

The server processes the requested operation and returns a JSON response containing either the calculation result or an error message.

TCP provides a reliable, ordered byte stream. The newline delimiter identifies the end of each application-level message.

## Testing

The application should be tested with:

- Valid IPv4 addresses and subnet prefixes.
- Different subnet sizes.
- IPv4 addresses from different classes.
- Invalid IP addresses and prefix lengths.
- Unsupported operation names.
- The TCP server being unavailable.
- Empty form submissions.

Automated test coverage and measured performance results should be documented after the tests have been implemented and executed.

## Limitations

- The application currently uses a loopback address and is intended for local demonstration.
- It focuses on IPv4 calculations.
- The TCP server is designed for a simple educational workload rather than high-concurrency production use.
- No authentication or encryption is implemented.
- Performance measurements have not been included in this document.

## Future Enhancements

- Add automated tests for all calculation functions.
- Add detailed request timing and performance analysis.
- Improve input validation and user-facing error messages.
- Extend support for additional network utilities.
- Add network packet analysis using Wireshark.

## Learning Outcomes

This project demonstrates the use of Python networking, TCP client-server communication, JSON message exchange, Flask integration, IPv4 addressing, subnet calculations, and modular software design.

## Author

**Project:** Socket-Based Network Calculator Service  
**Subject:** Computer Networks  
**Language:** Python

Add the project team's names, roll numbers, and other required academic details before submission.