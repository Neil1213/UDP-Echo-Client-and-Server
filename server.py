'''
Name: Neil Shah
UCID: ns642
Section: 005
'''
import sys
from socket import*

serverIP = "192.168.1.122"
serverPort = 8000
dataLen = 1000000

#Create a UDP socket
serverSocket = socket(AF_INET,SOCK_DGRAM)

#Assign IP address and port number to socket
serverSocket.bind((serverIP, serverPort))

print('The server is ready to recieve on port: '+str(serverPort))

#loop forever listening for incoming datagram messages
while True:
    #Recieve and print the client data from "data" socket
    data,address = serverSocket.recvfrom(dataLen)
    print("Recieve data from client "+address[0]+", "+str(address[1])+": "+data.decode())

    #Echo back to client
    print("Sending data to client "+address[0]+", "+str(address[1])+": "+data.decode())
    serverSocket.sendto(data,address)
