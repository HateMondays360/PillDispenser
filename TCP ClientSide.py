from socket import *
serverHost = "127.0.0.1" # Loopback address
serverPort = 12006
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost,serverPort))
while True:
    toServer = input()
    clientSocket.send(toServer.encode())
    if toServer == 'q':
        break
    fromServer = clientSocket.recv(1024).decode()
    print (fromServer)
clientSocket.close()
