#!/usr/bin/python
import socket
import multiprocessing
from sys import argv

portfile = 'serverports.txt'

#open service port to listen on
def opensocket(port_to_listen):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port_to_listen))
    server.listen(0)
    while True:
       connection, address = server.accept()
       print ("New connection from: ", address, " on port: ",port_to_listen)
       message = " pass"
       connection.send(message.encode('utf-8'))
       connection.close()


#generates a port list
def portlist():
    port_list = []
    with open(portfile, 'r') as file:
        for line in file:
            port_list.append(int(line))
    return port_list


def main():

    port_list = portlist()
    for port in port_list:
        process = multiprocessing.Process(target=opensocket, args=(port,))
        process.start()


main()

if __name__ == '__main__':
    pass
