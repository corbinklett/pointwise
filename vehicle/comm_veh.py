import numpy as np
import socket
import pickle

HEADERSIZE = 10

def connect(ip, port, client_type):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    client_socket.setblocking(False)
    client_type = client_type.encode('utf-8')
    client_type_header = f"{len(client_type):<{HEADERSIZE}}".encode('utf-8')
    client_socket.send(client_type_header + client_type)
    return client_socket