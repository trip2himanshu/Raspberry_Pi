# ./udp_server_client
# Python script for Raspberry Pi
# Himanshu Tripathi

# client side script using udp socket

import socket
import sys
import random
import time

# to run the server and client in different machines in a network
# give the server IP address in HOST of this script

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050

# method to create udp socket for client


def client_socket():
    try:
        # create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Client socket is ready")
        return sock
    except Exception as e:
        print("Error in client_socket: ", e)
        sys.exit()


# method to send data to server and receive ack message
def send_data(sock):
    while True:
        try:
            # generate dummy sensor data and convert it into string
            sensor_data = str(random.randint(1, 100))
            # send data to server
            sock.sendto(sensor_data.encode("utf-8"), (HOST, PORT))
            # receive message from server
            msg = sock.recvfrom(1024)
            if not msg:
                print("No ack received")
                break
            print(msg[0].decode("utf-8"))
            # wait for next data transmission
            time.sleep(5)
        except Exception as e:
            print("Error in send_data: ", e)
            break
        except KeyboardInterrupt:
            print("Client closed")
            break
    # clean exit
    sock.close()
    sys.exit()


# main script
if __name__ == "__main__":
    s = client_socket()
    send_data(s)
