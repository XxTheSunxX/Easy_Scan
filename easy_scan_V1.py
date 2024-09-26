# Easy Scan; Written by XxTheSunxX on August, 25. 2024, 
# Updated August, 30. 2024
# Simple Python Port Scanner.

import os
import sys
import socket
import time
from colorama import Fore

print(Fore.BLUE + """

███████╗ █████╗ ███████╗██╗   ██╗     ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝     ██╔════╝██╔════╝██╔══██╗████╗  ██║
█████╗  ███████║███████╗ ╚████╔╝      ███████╗██║     ███████║██╔██╗ ██║
██╔══╝  ██╔══██║╚════██║  ╚██╔╝       ╚════██║██║     ██╔══██║██║╚██╗██║
███████╗██║  ██║███████║   ██║███████╗███████║╚██████╗██║  ██║██║ ╚████║
╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                        
""")

print(Fore.WHITE + "")

def main():
    print("\n-Easy Scan-\n-Simple Python Port Scanner, Written by the XxTheSunxX-\n")

    IP = input("[*]Input IP to scan: ")
    list_ports = list(input("[*]Enter ports separated by space: ").strip().split())
    ports = map(int, list_ports)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    for port in ports:
        try:
            s.connect((IP, port))
            answer = s.recv(4028)
        except Exception as e:
            print(f"\n[*]Port {port} on {IP} is not open." )
            time.sleep(1)
        else:
            print(f"\n[*]Port {port} is open on IP Address {IP}.")
            print(f"[*]Message: {answer}")
            time.sleep(1)

    print("\n[*]Closing connection.")
    sys.exit()

if __name__ == '__main__':
    main()
