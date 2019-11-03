'''
Name: Neil Shah
UCID: ns642
Section: 005
'''
import sys, time
from socket import*

#Get the server hostname, port and data length as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]
count = argv[3]

#Command line argument is a string, change the port and count into integer
port = int(port)
count = int(count)
data = 'X'*count

#Create UDP client socket
clientsocket = socket(AF_INET, SOCK_DGRAM)

#Setting the socket timeout
clientsocket.settimeout(1)

for i in range(3):
    #Sending data to server
    print("Sending data to "+host+", "+str(port)+": "+data + " ("+str(count)+" characters)")
    clientsocket.sendto(data.encode(),(host,port))
    try:
        #Recieve the server response
        dataEcho,address = clientsocket.recvfrom(count)

        #Display the server response as an output
        print("Recieve data from " +address[0]+", "+str(address[1])+": "+dataEcho.decode())
        break
    except error:
        print("Message timed out")
#Close the client socket
clientsocket.close()
