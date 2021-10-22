from socket import *

serverAddress = '54.86.30.173'

serverPort = 5050

with socket(AF_INET, SOCK_DGRAM) as clientSocket:
    message = input("Masukkan sisi persegi: ")
    clientSocket.sendto(message.encode(),(serverAddress, serverPort))
    modifiedMessage, address = clientSocket.recvfrom(2048)
    print("Answer from server: ",modifiedMessage.decode())
    clientSocket.close()