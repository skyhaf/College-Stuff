from socket import *
serverName = '54.86.30.173'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print("Fungsi menghitung luas persegi")
sentence = input('Input sisi persegi: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('Answer From Server: ', modifiedSentence.decode())
clientSocket.close()
