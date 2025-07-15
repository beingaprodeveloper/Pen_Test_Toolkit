import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((target, port))
            print(f"[OPEN] Port {port}")
        except:
            pass
        s.close()
