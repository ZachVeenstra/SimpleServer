import socket
from datetime import datetime

"""Credit to https://docs.python.org/3/howto/sockets.html
for teaching me the basics of socket programming."""

print("The Server is running")

# Creates the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binds the socket's address to an arbitrary port number.
server.bind((socket.gethostname(), 5013))

# Accepts one request for connection.
server.listen(1)

# run until KeyboardInterupt.
try:
    while True:

        # Accept the client's address.
        (client, address) = server.accept()

        # Receive a message from the client.
        msg = client.recv(1024).decode()

        # Print the message.
        print(msg)

        # Create a datetime String.
        dt = str(datetime.now())

        # And send it to the client.
        client.send(dt.encode())

except KeyboardInterrupt:
    server.close()