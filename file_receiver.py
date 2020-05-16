import socket
#create socket
s=socket.socket()
port=180
#binding the socket to the particular port, so that any request will be connected to the particular server socket.
s.bind(('',port))
# listen will allow no.of connections to be established
s.listen(1)
while True:
    # accepting the connection . c here is used for sending and receiving connection , addr is the address bound to the socket.
    c,addr=s.accept()
    # recv is an inbuilt-function of socket which accepts parameter of how much byte of data it can take
    DataReceived=c.recv(4096)
     # open file 'newFile.txt' in write binary mode and address is as src
    with open("newFile.txt", "wb") as src:
        # writes data in bytes 
        src.write(DataReceived)
        # close the opened file
        src.close()
    # data to be sent has to be in bytes , converting data to byte is encoding
    c.send("File received".encode())
    # closing the connection
    c.close()
# closing connection with socket    
s.close()
