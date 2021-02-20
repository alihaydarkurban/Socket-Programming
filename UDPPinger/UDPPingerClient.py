# ####################################################################################################
#
# File:		UDPPingerClient.py
# Author:	Ali Haydar KURBAN
# Date: 	February 2021
# Language: Python
# Version:  2.7.18
#
# ####################################################################################################

from socket import *
import time

# Message text
message_text = 'ping'

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# To get the client wait up to one second
clientSocket.settimeout(1)

# Creating IP address and port number
addr = ('localhost', 12000)

# Sending 10 message to the server.
for i in range(10):
    send_time = time.time()
    message_to_send = '{} {} {}'.format(message_text, (i + 1), time.strftime("%H:%M:%S"))
    clientSocket.sendto(message_to_send, addr)

    print '========================================================'
    try:
        received_message, server = clientSocket.recvfrom(1024)
        received_time = time.time()
        RTT = received_time - send_time
        print 'Message to Send: \'{}\''.format(message_to_send)
        print 'Response Message: \'{}\''.format(received_message)
        print 'Round Trip Time: {}'.format(RTT)

    except timeout:
        print 'Request Timed Out {}'.format(i + 1)
    print '========================================================'

clientSocket.close()
