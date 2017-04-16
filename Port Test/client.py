#!/usr/bin/python
import socket
from sys import argv
import getopt

portfile = 'clientports.txt'

def open_socket(ports, server_ip):
    client_socket = socket.socket()
    client_socket.settimeout(5)
    #host = socket.gethostname()
    try:

        client_socket.connect((server_ip, ports))
        print(ports, client_socket.recv(4096).decode('utf-8'))
        client_socket.close
    except socket.error:
        print(ports, " fail")


#generates a port list
def portlist():
    port_list = []
    with open(portfile, 'r') as file:
        for line in file:
            port_list.append(int(line))
    return port_list


def main(argv):
    server_ip = argv[1]
    port_list = portlist()
    for port in port_list:
        open_socket(port, server_ip)


main(argv)


if __name__ == '__main__':
    pass
