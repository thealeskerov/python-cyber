# Simple TCP Port Scanner using sockets

import socket

def scan_ports(host, ports):
    print(f"Scanning {host}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # timeout for response
            result = sock.connect_ex((host, port))  # try connecting
            if result == 0:
                print(f"Port {port} is OPEN")
            sock.close()
        except socket.error:
            print(f"Couldn't connect to {host}")
            break

# User input
target = input("Enter target IP or hostname: ")
port_range = range(20, 1025)  # Common ports
scan_ports(target, port_range)
