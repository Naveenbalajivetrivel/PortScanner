import socket          #pip install sockek
from IPy import IP     #pip install IPy

def scan(target):
    converted_ip = check_ip(target)
    print('\n [-_0] Scanning Target ' + str(target))
    for port in range(1, 101):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError :
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)
def  scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[^=^] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[^=^] Open Port ' + str(port))
    except:
        pass

if __name__ == "__main__":
    targets = input('[^-^] Enter the Target/s IP (split muntiple targets with , ) : ')
    if ',' in targets:
        for ip_address in targets.split(','):
            scan(ip_address.strip(' '))
    else:
        scan(targets)


