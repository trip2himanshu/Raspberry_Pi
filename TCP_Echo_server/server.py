# ./TCP_Echo_server
# server.py
# Python script for Raspberry Pi
# Himanshu Tripathi

# TCP echo server
# receives the message from client and echo back the same to client

import socket
import sys

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050


def server_socket():
    try:
        # create TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket
        sock.bind((HOST, PORT))
        # listen for clients
        sock.listen()
        sock.setsockopt(socket.SO_REUSEADDR)
        print(f"Server is up and running at {HOST}:{PORT}")
        return sock
    except Exception as e:
        print(f"Error in socket creation : {e}")
        sys.exit()


def echo_server(sock):
    while True:
        try:
            client, addr = sock.accept()
            print(f"Client connected from {addr[0]}:{addr[1]}")
            while True:
                try:
                    msg = client.recv(1024)
                    if not msg:
                        print("No message received")
                        break
                    print(
                        f"{addr[0]}:{addr[1]} >> {msg.decode('utf-8')}".decode("utf-8")
                    )
                    # echo back the message
                    client.send(f"Server >> {msg}")
                except Exception as e:
                    print(f"Error in echo_server : {e}")
                    break
                except KeyboardInterrupt:
                    print("client connection interrupted")
                    break
            client.close()
        except KeyboardInterrupt:
            print("server is going down")
            break
    sock.close()
    sys.exit()


if __name__ == "__main__":
    s = server_socket()
    echo_server(s)
