import socket
#creating socket
sock = socket.socket()
port = 860
#binding the socket to the particular port, so that any request will be connected to the particular server socket.
sock.bind(('', port))
# listen will allow no.of connections to be established
sock.listen(1)

while True:
    # accepting the connection . c here is used for sending and receiving connection , addr is the address bound to the socket.
    c, addr = sock.accept()
    print("Connection recieved from", str(addr))
    # recv is an inbuilt-function of socket which accepts parameter of how much byte of data it can take    
    MessageReceived = c.recv(4096)
    # as severs exchange data in bytes, convert data for user readability
    # converting from byte form into any other form is decoding
    PrintMessage=MessageReceived.decode()
    print(PrintMessage)
    message = "Hello sender!"
    # data to be sent has to be in bytes , converting data to byte is encoding    
    c.send(message.encode())
    # closing the connection
    c.close()
# closing connection with socket    
sock.close()