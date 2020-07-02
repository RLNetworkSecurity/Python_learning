#server code (unencrypted)

from socket import *

#create a socket (IPV4)
my_socket = socket(AF_INET, SOCK_STREAM, 0)

ipv4_tuple = "127.0.0.1", 1066

#bind the socket Server connection
my_socket.bind(ipv4_tuple)

#get it to listen!
my_socket.listen(1)

#accepting a connection
print(f"waiting for connection on port {ipv4_tuple[1]}")
new_socket_object, r_address = my_socket.accept()

print(f"Connection made from: ", r_address)
recieved_data = new_socket_object.recv(4096, 0)
