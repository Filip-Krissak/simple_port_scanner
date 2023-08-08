import socket
import pyfiglet
import sys
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

def connScan():
    try:
        socket.setdefaulttimeout(0.5)
        for port in range(1,65535):
            connskt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            result = connskt.connect_ex((target,port))
            if result == 0:
                print('[+] tcp open:', port)
            connskt.close()
    except KeyboardInterrupt:
            print('\n Exiting... ')
            sys.exit()
    except socket.error:
            print('\n Host is not responding... ')
            sys.exit()

if __name__ == '__main__':
    connScan()