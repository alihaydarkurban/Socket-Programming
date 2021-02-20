# ####################################################################################################
#
# File:     WebServer.py
# Author:   Ali Haydar KURBAN
# Date:     February 2021
# Language: Python
# Version:  2.7.18
#
# ####################################################################################################

# Import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
# Open cmd and enter 'ipconfig'
# Inside the 'Wireless LAN adapter Wi-Fi:'
# There is IPv4 Address address
# Before test the program, change the IPv4_ADDRESS with yours.
IPv4_ADDRESS = 'example_IPv4'
port_number = 6789
serverSocket.bind((IPv4_ADDRESS, port_number))
serverSocket.listen(1)

# Print information about the server socket and example usage
print 'IPv4 Address =', IPv4_ADDRESS
print 'Port Number =', port_number
print 'Example Usage = {}:{}/HelloWorld.html'.format(IPv4_ADDRESS, port_number)

while True:
    # Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        # print message
        if len(message) > 1:
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            # print outputdata
            f.close()

            # Send one HTTP header line into socket
            connectionSocket.send('HTTP/1.1 200 OK\r\n')
            connectionSocket.send('Content-Type: text/html\r\n\r\n')

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i])
            connectionSocket.close()

    except IOError:
        # Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n')

        # Close client socket
        connectionSocket.close()

serverSocket.close()
