import socket


def get_hostname_IP():
    hostname=input("Enter a website name: ")
    try:
        print(f'Hostname:{hostname}')
        print(f'IP:{socket.gethostbyname(hostname)}')
        
    except socket.gaierror as error:
        print(f'Invalid hostname, error raised is {error}')
        
get_hostname_IP()