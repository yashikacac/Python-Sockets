import socket
# create socket
s=socket.socket()
# defining a port to which socket connects to the server in local computer 
s.connect(('localhost',180))
# open file 'details.txt' in read binary mode and assign it as file
with open('details.txt','rb') as file:
    # the data of file will be read in bytes
    data=file.read()
    # send data of the file
    s.send(data)
    # closing the opened file
    file.close()
# recv is an inbuilt-function of socket which accepts parameter of how much byte of data it can take     
messageReceived = s.recv(4096)
# as severs exchange data in bytes, convert data for user readability
# converting from byte form into any other form is decoding    
decodedMessage = messageReceived.decode()
print(decodedMessage)
# close connection with socket
s.close()
