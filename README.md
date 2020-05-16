# Python Sockets

This repository is an attempt to learn socket programming in Python. I learned about how sockets work, how a connection between sockets can be established, how messages can be sent and received. Also tried transferring a text file from socket to socket.

- The ```server.py```, and the ```receiver.py``` files are used to create two sockets which listen on two different ports. The  ```google_socket.py``` file connects with the socket created by the ```receiver.py``` file and sends the bytes read from a file. The ```receiver.py``` file decodes the message received and prints the decoded message. Then, the ```google_socket.py``` file connects with the ```server.py``` file and encodes a message and sends it. The message received is decoded and then printed.
- The ```file_receiver.py``` listen to a particular socket port. The ```file_sender.py``` file connects with it and establishes a connection. A file is read, and the bytes are sent to the socket created by ```file_receiver.py```. The bytes are then written to a new file thus transferring a file from one socket to another.

## Requirement
Any system with python 3 (preferably 3.6) and terminal.

## Usage
- Running ```python file_name.py``` or ```python3 file_name.py``` where file_name.py can be any file from the listed files.
- If you are trying any of the file transfer methods, be sure to create a file called details.txt so that the files can refer to for transferring the file.

## License
> The MIT License