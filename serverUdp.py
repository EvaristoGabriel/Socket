from socket import *

# configurando o servidor
serverName = 'localhost'
serverPort = 12000

serverSocket = socket(AF_INET,SOCK_DGRAM)

serverSocket.bind((serverName,serverPort))

print("O servidor está pronto para receber")
try :
    while True:
        print("Esperando")
        message, clientAdress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper()
        splittedSum = modifiedMessage.split('+')
        sum = int(splittedSum[0]) + int(splittedSum[1])
        newMessage = str(sum)
        serverSocket.sendto(newMessage.encode(),clientAdress)
        print("Mensagem enviada ao cliente...")

except KeyboardInterrupt:
        print("\nServidor encerrado pelo usuário")

finally:
    serverSocket.close()
    print("Socket fechado")



