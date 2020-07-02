#client code (unencrypted)

from socket import *

#setting up network requirements
my_socket = socket(AF_INET, SOCK_STREAM, 0)
ipv4_tuple = "127.0.0.1", 1066

#try connecting
my_socket.connect(ipv4_tuple)

#send a message (stream of bytes)
print("Sending message.....")
input_message = input("input your message:")
encoded_message = bytes(input_message, 'ascii')

my_socket.send(encoded_message, 0)

#close connection
print("Closing the connection!")
my_socket.close()
