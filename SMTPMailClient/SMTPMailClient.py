# ####################################################################################################
#
# File:		SMTPMailClient.py
# Author:	Ali Haydar KURBAN
# Date: 	February 2021
# Language: Python
# Version:  2.7.18
#
# ####################################################################################################

from socket import *
import base64
import ssl
from datetime import datetime

sender_mail_address = 'sender_mail@example.com'
sender_mail_password = '**********'
receiver_mail_address = 'receiver_mail@example.com'

# Choose a mail server (Google mail server) and call it mail server
mailserver = ('smtp.gmail.com', 587)

# Create socket called clientSocket and establish a TCP connection with mail server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.\n'

# Send HELO command and print server response.
HELO = 'HELO Alice\r\n'
clientSocket.send(HELO)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.\n'


# Google mail server requires these for authentication and security reasons.
STARTTLS = 'STARTTLS\r\n'
clientSocket.send(STARTTLS)
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '220':
	print '220 reply not received from server.\n'
clientSocket = ssl.wrap_socket(clientSocket)


# Authentication for your e-mail account.
base64_str = ('\x00' + sender_mail_address + '\x00' + sender_mail_password)
base64_str = base64.b64encode(base64_str)
base64_str = base64_str.strip('\n')
AUTH_PLAIN = 'AUTH PLAIN ' + base64_str + '\r\n'
clientSocket.send(AUTH_PLAIN)
recv3 = clientSocket.recv(1024)
print recv3
if recv3[:3] != '235':
	print '235 reply not received from server.\n'


# Send MAIL FROM command and print server response.
MAIL_FROM = 'MAIL FROM:<' + sender_mail_address + '>\r\n'
clientSocket.send(MAIL_FROM)
recv4 = clientSocket.recv(1024)
print recv4
if recv4[:3] != '250':
	print '250 reply not received from server.\n'


# Send RCPT TO command and print server response.
RCPT_TO = 'RCPT TO:<' + receiver_mail_address + '>\r\n'
clientSocket.send(RCPT_TO)
recv5 = clientSocket.recv(1024)
print recv5
if recv5[:3] != '250':
	print '250 reply not received from server.\n'


# Send DATA command and print server response.
DATA = 'DATA\r\n'
clientSocket.send(DATA)
recv6 = clientSocket.recv(1024)
print recv6
if recv6[:3] != '354':
	print '354 reply not received from server.\n'


# Send message data.
subject_name = 'SMTPMailClient Test'
subject = 'Subject: {}\r\n\r\n'.format(subject_name)
clientSocket.send(subject)
now = datetime.now()
message = now.strftime("%B %d, %Y %H:%M:%S")
message = 'You can check the e-mail with that time: ' + message
author = '\r\nAli Haydar KURBAN\r\n'
clientSocket.send(message)
clientSocket.send(author)
print '=================================================================================='
print 'The context of the e-mail must be like these'
print '----------------------------------------------'
print message,    # Printing without new line
print author,  # Printing without new line
print '==================================================================================\n'


# Message ends with a single period.
endmsg = '\r\n.\r\n'
clientSocket.send(endmsg)
recv7 = clientSocket.recv(1024)
print recv7
if recv7[:3] != '250':
	print '250 reply not received from server.\n'


# Send QUIT command and get server response.
QUIT = 'QUIT\r\n'
clientSocket.send(QUIT)
recv8 = clientSocket.recv(1024)
print recv8
if recv8[:3] != '221':
	print '221 reply not received from server.\n'

clientSocket.close()
