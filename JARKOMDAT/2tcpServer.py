from socket import *
import random
serverPort = 12000
with socket(AF_INET, SOCK_STREAM) as serverSocket:
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)

    dict_session = {}
    pesan = ""
    
    def convertTuple(tup):
        str = ''.join(tup)
        return str

    print('The server is ready to receive')
    while(True):
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode().split(" ")
        input = sentence[0]
        output = sentence[2:]

        if(input == "LOGIN"):
            nama = sentence[1]
            id_session = random.randint(1,100)
            dict_session[id_session] = nama
            pesan = "NEW_SESSION " + str(id_session)

        if(input == "MSG"):
            key_compare = sentence[2]
            for key,value in dict_session.items():
                if(key == key_compare):
                    pesan_keluar = ' '.join(map(str,output))
                    pesan = "ANSWER " + key + " " + pesan_keluar
                
                else:
                    pesan = "ANSWER Y0u are not logged in"

        pesan = convertTuple(pesan)
        print(pesan)
        connectionSocket.send(pesan.encode())

        connectionSocket.close()
        