import socket

def scan(target, ports):
    """
    Scan a range of ports on a target host.

    :param target: The target host's IP address.
    :param ports: The number of ports to scan.
    """
    print('\n' + 'Starting Scan For ' + str(target))
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    """
    Scan a specific port on a target host.

    :param ipaddress: The target host's IP address.
    :param port: The port to scan.
    """
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        pass

targets = input("[*] Enter Targets To Scan (split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)

