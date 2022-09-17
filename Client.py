import socket

"""Credit to https://docs.python.org/3/howto/sockets.html
for teaching me the basics of socket programming."""

# Create the client socket.
client = socket.socket()

print("Enter the server's IP:")

# Prompts for the user to enter in the desired IP.
ip = input()

# Connects the client to the server.
client.connect((ip, 5013))

# Run the message loop until KeyboardInterrupt.
try:
    while True:

        # Send message to the server.
        client.send("Received".encode())

        # Receive message from server.
        msg = client.recv(1024).decode()

        # Print the received message.
        print(msg)

except KeyboardInterrupt:
    client.close()