# import socket module
import socket
# import sys module
import sys
try:
    # create socket
    s = socket.socket()
    print("Socket Successfully created")
    # looking out if a socket error occurs   
except socket.error as err:
    print("socket creation failed with error")
# defining a port to which socket connects to the server in local computer 
s.connect(('localhost', 181))
# open file 'details.txt' in read binary mode and assign it as file
with open("details.txt", "rb") as file:
    # the data of file will be read in bytes
    data = file.read()
    # send data of the file    
    s.send(data)
    # closing the opened file    
    file.close()
    # recv is an inbuilt-function of socket which accepts parameter of how much byte of data it can take   
bytesOurServerSends = s.recv(4096)
# as severs exchange data in bytes, convert data for user readability
# converting from byte form into any other form is decoding
whatOurServerSays = bytesOurServerSends.decode()
print(whatOurServerSays)
# close connection with socket
s.close()
print("Closing connection with socket")
print("Creating a new socket and establishing a new connection")
# create another socket
s = socket.socket()
# defining a port to which socket connects to the server in local computer
s.connect(('localhost', 860))
message = "Hello, text receiver"
# data to be sent has to be in bytes , converting data to byte is encoding
s.send(message.encode())
# recv is an inbuilt-function of socket which accepts parameter of how much byte of data it can take
bytesOurServerSends = s.recv(4096)
# as severs exchange data in bytes, convert data for user readability
whatOurServerSays = bytesOurServerSends.decode()
print(whatOurServerSays)
# close connection with socket
s.close()