# UDPPinger
##### It a server-client project that sends and receives datagram packets using UDP sockets and also sets a proper socket timeout.
***
#### Features of UDPPingerServer
* It sits in an infinite loop listening for incoming UDP packets. 
* When a packet comes in;
  - If a randomized integer is greater than or equal to 4, the server simply capitalizes the data and sends it back to the client.
  - Otherwise, packets are simulated to be lost.
***
#### Features of UDPPingerClient
* It sends 10 pings to the server.
* It waits up to one second for a reply;
  - If no reply is received within one second, then the client assumes that the packet was lost during transmission.
  - Otherwise, the client prints the response message from server, calculates and prints the round trip time (RTT).
* `localhost`is used to send and receive the packets.
* The client's message is one line, consisting of ASCII characters in the following format: `Ping sequence_number time`
* `Ping` is a string of ASCII characters.
* `sequence_number` starts at 1 and progresses to 10 for each successive ping message sent by the client.
* `time` is the time when the client sends the message.
***
#### Running
*You have to run [UDPPingerServer.py](https://github.com/alihaydarkurban/Socket-Programming/blob/main/UDPPinger/UDPPingerServer.py) first, after that you can run [UDPPingerClient.py](https://github.com/alihaydarkurban/Socket-Programming/blob/main/UDPPinger/UDPPingerClient.py)* <br/>
Open your terminal for UDPPingerServer.py and go to the same path with the files and typed this:
```
py -2 UDPPingerServer.py
```
Open another terminal for UDPPingerClient.py and go to the same path with the files and typed this:
```
py -2 UDPPingerClient.py
```
***
