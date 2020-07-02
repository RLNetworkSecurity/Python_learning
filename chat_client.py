#client code (unencrypted)

from socket import *

#setting up network requirements
my_socket = socket(AF_INET, SOCK_STREAM, 0)
ipv4_tuple = "127.0.0.1", 1066

#try connecting
my_socket.connect(ipv4_tuple)

#if statement to keep giving an option for chat

while True:
    input_message = input("To exit type quit, or input your message: ")
    
    if input_message == "quit":
        break
    else:
        encoded_message = bytes(input_message, 'ascii')
        print("Sending you message")
        my_socket.send(encoded_message, 0)

encoded_message = bytes(input_message, 'ascii')
my_socket.send(encoded_message, 0)
print("The Client has chosen to Close this connection!")
my_socket.close()
