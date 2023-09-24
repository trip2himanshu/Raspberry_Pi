# ./udp_server_client
# Python script for Raspberry Pi
# Himanshu Tripathi

# server side script using udp socket
# udp socket is created and server receives the data from client


import socket
import sys

# to run the server and client on different machines in a network
# it is advised to check the server IP address using command
# hostname -I
# write HOST = "<IP_ADDR>"

# HOST = socket.gethostbyname(socket.gethostname())
HOST = "192.168.29.96"
PORT = 5050

# method to create udp socket for server


def server_socket():
    try:
        # create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # bind the server
        sock.bind((HOST, PORT))
        print("Server is up and running at ", HOST)
        return sock
    except Exception as e:
        print("Error in socket cretion : ", e)
        sys.exit()


# method to receive data from client
def get_data(sock):
    while True:
        try:
            # receive data
            # received data is in tupple format having data and client addr
            recv_data = sock.recvfrom(1024)
            data = recv_data[0]
            addr = recv_data[1]
            print(data)
            print(addr)
            # send acknowledgement message to client
            # addr should be in tupple format
            sock.sendto("received".encode("utf-8"), addr)
        except Exception as e:
            print("Error in get_data: ", e)
        except KeyboardInterrupt:
            print("Server shutdown")
            break
    # clean exit
    sock.close()
    sys.exit()


# main script
if __name__ == "__main__":
    s = server_socket()
    get_data(s)
