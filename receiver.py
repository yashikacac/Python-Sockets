import socket
#creating socket
soc = socket.socket()
port = 181
#binding the socket to the particular port, so that any request will be connected to the particular server socket.
soc.bind(('',port))
# listen will allow no.of connections to be established
soc.listen(1)

while True:
    # accepting the connection . c here is used for sending and receiving connection , addr is the address bound to the socket.  
    c, addr = soc.accept()
    print("Connection recieved from", str(addr))
    # recv is an inbuilt-function of socket which accepts parameter of how much byte of data it can take     
    dataReceived = c.recv(4096)
    # as severs exchange data in bytes, convert data for user readability
    # converting from byte form into any other form is decoding    
    decodedMessage = dataReceived.decode()
    print(decodedMessage)
    message = "Message Received"
    # data to be sent has to be in bytes , converting data to byte is encoding    
    c.send(message.encode())
    # closing the connection    
    c.close()
    # closing connection with socket    
soc.close()