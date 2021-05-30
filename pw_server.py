import socket
import select
import pickle
import numpy as np

HEADER_LENGTH = 10

# should have incoming data coming to this file from client: image processor/filter

IP = "127.0.0.1"
PORT = 1235

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# For a server using 0.0.0.0 means to listen on all available interfaces, useful to connect locally to 127.0.0.1 and remotely to LAN interface IP
server_socket.bind((IP, PORT))
server_socket.listen()
sockets_list = [server_socket]

vehicle_clients = []
sensor_clients = []

print(f'Listening for connections on {IP}:{PORT}...')

# Handles message receiving
def receive_message(client_socket):

    try:

        # Receive our "header" containing message length, it's size is defined and constant
        message_header = client_socket.recv(HEADER_LENGTH)
        # If we received no data, client gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
        if not len(message_header):
            return False
        # Convert header to int value
        message_length = int(message_header.decode('utf-8').strip())
        # Return an object of message header and message data
        return {'header': message_header, 'data': client_socket.recv(message_length)}
    except:
        return False

def receive_pickled_message(client_socket):

    try:

        # Receive our "header" containing message length, it's size is defined and constant
        message_header = client_socket.recv(HEADER_LENGTH)

        # If we received no data, client gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
        if not len(message_header):
            return False

        # Convert header to int value
        message_length = int(message_header.decode('utf-8').strip())
        message = client_socket.recv(message_length)
        return message_length, message, pickle.loads(message)

    except:
        return False

while True:
    # Calls Unix select() system call or Windows select() WinSock call with three parameters:
    #   - rlist - sockets to be monitored for incoming data
    #   - wlist - sockets for data to be send to (checks if for example buffers are not full and socket is ready to send some data)
    #   - xlist - sockets to be monitored for exceptions (we want to monitor all sockets for errors, so we can use rlist)
    # Returns lists:
    #   - reading - sockets we received some data on (that way we don't have to check sockets manually)
    #   - writing - sockets ready for data to be send thru them
    #   - errors  - sockets with some exceptions
    # This is a blocking call, code execution will "wait" here and "get" notified in case any action should be taken
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    #for notified_socket in read_sockets:

        # get header to see if it is car or pw device
        # if read_socket:

    # Iterate over notified sockets
    for notified_socket in read_sockets:

        # If notified socket is a server socket - new connection, accept it
        if notified_socket == server_socket:

            # Accept new connection
            # That gives us new socket - client socket, connected to this given client only, it's unique for that client
            # The other returned object is ip/port set
            client_socket, client_address = server_socket.accept()

            # Add accepted socket to select.select() list
            sockets_list.append(client_socket)

            print('Accepted new connection from {}:{}'.format(*client_address))
            
            # get the client ID - then should save client ID to a list
            msg = receive_message(client_socket)


            # If False - client disconnected before he sent his name
            if msg is False:
                continue

            # Add accepted socket to select.select() list
            sockets_list.append(client_socket)

            # Also save username and username header
            if msg['data'].decode('utf-8') == "s":
                #sensor_clients[client_socket] 
                sensor_clients.append(client_socket)
                print("as a sensor")
            elif msg['data'].decode('utf-8') == "v":
                vehicle_clients.append(client_socket)
                print("as a vehicle")


        # Else existing socket is sending a message (and is pickled)
        else:
            # Receive message - ASSUME IT IS PICKLED DATA FROM SENSOR
            message = receive_pickled_message(notified_socket)

            # If False, client disconnected, cleanup
            if message is False:
                print('Closed connection from: ')

                # Remove from list for socket.socket()
                sockets_list.remove(notified_socket)

                # Remove from our list of users
                # del clients[notified_socket]

                continue

            # broadcast sensor data to clients
            unpickled_data = message[2]
            print(unpickled_data)

            pickled_data = message[1]
            message_len = message[0]
            # broadcast message to "vehicle" subscibers
            for vehicle_socket in vehicle_clients:
                msg = bytes(f"{message_len:<{HEADER_LENGTH}}", 'utf-8') + pickled_data
                vehicle_socket.send(msg)


    # It's not really necessary to have this, but will handle some socket exceptions just in case
    for notified_socket in exception_sockets:

        # Remove from list for socket.socket()
        sockets_list.remove(notified_socket)

        # Remove from our list of users
        # del clients[notified_socket]