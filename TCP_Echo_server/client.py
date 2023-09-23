# ./TCP_Echo_server
# client.py
# Python script for Raspberry Pi
# Himanshu Tripathi

# TCP client
# connects with server and communicate messages

import socket
import sys

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050


def client_socket():
    try:
        # create TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect with server
        sock.connect((HOST, PORT))
        print("Connection established with server")
        return sock
    except Exception as e:
        print(f"Error in socket creation : {e}")
        sys.exit()


def communication(sock):
    while True:
        try:
            sock.send(input(">> ").encode("utf-8"))
            msg = sock.recv(1024)
            if not msg:
                print("No message received")
                break
            print(msg.decode("utf-8"))
        except Exception as e:
            print(f"Error in echo_server : {e}")
            break
        except KeyboardInterrupt:
            print("client connection interrupted")
            break
    sock.close()
    sys.exit()


if __name__ == "__main__":
    s = client_socket()
    communication(s)
