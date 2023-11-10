import socket

def scan(target, ports):
    """
    Scan a range of ports on a single target host.

    param target: The target host's IP address.
    param ports: The number of ports to scan.
    """
    print('\n' + 'Starting Scan For ' + str(target))
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    """
    Scan a specific port on a single target host.

    param ipaddress: The target host's IP address.
    param port: The port to scan.
    """
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        pass

target = input("[*] Enter the Target IP Address: ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

scan(target, ports)
