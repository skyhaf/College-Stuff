from socket import *
serverName = '18.233.170.114'
serverPort = 12000


with socket(AF_INET, SOCK_STREAM) as clientSocket:
    clientSocket.connect((serverName,serverPort))
    sentence = input("Masukkan perintah: ")
    clientSocket.send(sentence.encode())
    modifiedMessage = clientSocket.recvfrom(1024)
    print(modifiedMessage)
    clientSocket.close()

