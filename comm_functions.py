import localizer_params as param
import numpy as np
import socket
import pickle

HEADERSIZE = 10

def connect(ip, port, client_id):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    client_socket.setblocking(False)
    client_id = client_id.encode('utf-8')
    client_id_header = f"{len(client_id):<{HEADERSIZE}}".encode('utf-8')
    client_socket.send(client_id_header + client_id)
    return client_socket

def broadcast_data(data, my_socket):
    # pickles data and sends it out via my_socket

    msg = pickle.dumps(data)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg
    my_socket.send(msg)
    
    # return true if message send was successful?