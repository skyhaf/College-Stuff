from socket import *

serverPort = 5050

with socket(AF_INET, SOCK_DGRAM) as serverSocket:
    serverSocket.bind(('', serverPort))
    print('The server is ready to receive')
    
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        message = int(message)
        print('Message from client',message)
        hasil = message * message
        hasil = str(hasil)
        print('Answer from Server',hasil)
        serverSocket.sendto(hasil, clientAddress)