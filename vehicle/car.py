import errno
import comm_veh as comm
import sys
import pickle

HEADER_LENGTH = 10

HEADERSIZE = 10 
IP = "127.0.0.1"
PORT = 1235
CLIENT_TYPE = "v"

# connect to server
client_socket = comm.connect(IP, PORT, CLIENT_TYPE)

while True:

    try:
        # Now we want to loop over received messages (there might be more than one) and print them
        while True:

            # receive messages from server
            message_header = client_socket.recv(HEADER_LENGTH)

            # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
            if not len(message_header):
                print('Connection closed by the server')
                sys.exit()

            message_length = int(message_header.decode('utf-8').strip())
            pickled_message = client_socket.recv(message_length)
            print(pickle.loads(pickled_message))



    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()