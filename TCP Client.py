from socket import * #import everything from socket
                    #to avoid having socket as a prefix to its objects
import json
serverHost = "127.0.0.1" #Loopback address
serverPort = 12006
serverSocket = socket(AF_INET,SOCK_STREAM) #create TCP welcoming socket
serverSocket.bind((serverHost,serverPort))
serverSocket.listen(1) # 1 is the backlog parameter that specifies the maximum number # of connections requests that the kernel should queue
                        # for this socket waiting for completion of the connection.
print ("The server is ready to receive")
connectionSocket, addr = serverSocket.accept() #waits on for incoming requests
                                                #new socket created on return
print ("Connection from: " + str(addr))
conversions=[[1, 0.81, 1.25, 0.72], [1.24, 1, 1.55, 0.89], [0.8, 0.64, 1, 0.57], [1.4, 1.13, 1.75, 1]]
mappings={'USD' :0, 'EUR': 1, 'CAD':2, 'GBP':3}
while True: #loop forever
    fromClient = connectionSocket.recv(1024).decode().upper() # wait until (blocking socket) receiving a max of 1024
                                                    # bytes at a time and decode the received UTF‐8 string
                                                    # to Unicode string.
                                                    # Unicode text is the default string type in Python 3
    if fromClient == 'q':
        break
    elif fromClient =='?':
        connectionSocket.send(b'USD \t United States Dollar\n')
        connectionSocket.send(b'EUR \t Euro\n')
        connectionSocket.send(b'Cad \t Canadian Dollar\n')
        connectionSocket.send(b'GBP \t United Kingdom Pound\n')
        connectionSocket.send(b'To exchange currency enter: <amount> <cur1> <cur2>')
    else:
        try:
            parts=fromClient.split()
            value=parts[0]
            result=float(int(value)*conversions[mappings[parts[1]]][mappings[parts[2]]])
            connectionSocket.send((str(value)+' '+parts[1]+' = '+str(result)+' '+parts[2]).encode())
        except ValueError:
            connectionSocket.send(b'Error!')
        except KeyError:
            connectionSocket.send(b'Error!')
connectionSocket.close() #close connection to this client
                        #(but not welcoming socket)
