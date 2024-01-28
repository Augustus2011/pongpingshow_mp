import socket
from _thread import *
import _thread
import os
import sys

server="192.168.1.192"
port=8000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.bind((server,port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("waiting for a connection, server started")

def threaded_client(conn):
    conn.send(str.encode("connected"))
    reply=""
    while True:
        try:
            data=conn.recv(2048)
            reply=data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("recieved",reply)
                print("sending :",reply)
            conn.sendall(str.encode(reply))
        except:
            break
    print("lost connection")
    conn.close()

while True:
    conn,addr=s.accept()
    print("Connected to:",addr)
    start_new_thread(threaded_client,(conn,))