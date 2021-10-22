from socket import *
serverPort = 12000
with socket(AF_INET, SOCK_STREAM) as serverSocket:
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print('The server is ready to receive')
    while(True):
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        sentence = sentence.decode()
        sentence = int(sentence)
        hasil = sentence * sentence
        hasil = str(hasil)
        connectionSocket.send(hasil.encode())
        connectionSocket.close()