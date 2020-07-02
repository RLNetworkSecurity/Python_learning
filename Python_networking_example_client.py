#client code (unencrypted)

from socket import *

#setting up network requirements
my_socket = socket(AF_INET, SOCK_STREAM, 0)
ipv4_tuple = "127.0.0.1", 1066

#try connecting
my_socket.connect(ipv4_tuple)

#send a message (stream of bytes)
print("Sending message.....")
msg = b"Hello from batcave"

my_socket.send(msg, 0)

#close connection
print("Closing the connection!")
my_socket.close()
