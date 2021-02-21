# WebServer
##### It is a simple Web Server that is capable of processing only one request with TCP connection.
***
#### Features of WebServer 
* It creates a connection socket when contacted by a client which is a browser.
* It receives the HTTP request from this connection.
* It parses the request to determine the specific file being requested.
* It gets the requested file from the server's file system.
* It creates an HTTP response message consisting of the requested file preceded by header lines.
* It sends the response over the TCP connection to the requesting browser.
* If a browser requests a file that is not present in the server, the it returns a "404 Not Found" error message.
***
#### Before Running
You have to change IPv4_ADDRESS in the [WebServer.py](https://github.com/alihaydarkurban/Socket-Programming/blob/main/WebServer/WebServer.py) with yours. The following code statement shows you how to find IPv4 Address:
```
# Open cmd and enter 'ipconfig'
# Inside the 'Wireless LAN adapter Wi-Fi:'
# There is IPv4 Address address
# Before test the program, change the IPv4_ADDRESS with yours.
```
***
#### Running
Open your terminal, go to the same path with the files and enter this:
```
py -2 WebServer.py
```
***
