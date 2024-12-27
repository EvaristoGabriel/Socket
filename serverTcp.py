from socket import *
import threading

# configurando o servidor
serverName = 'localhost'
serverPort = 3333

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)

def receiveMessage(conexaoSocket):
     while True:
        try: 
            mensagem = conexaoSocket.recv(2048).decode()
            if mensagem:
                print(f'Cliente: {mensagem}')
            else:
                 break
        except:
             print("Conexão encerrada")
             break

def sendMessage(conexadoSocket):
     while True:
          mensagem = input("Servidor: ")
          conexadoSocket.send(mensagem.encode())



conexaoSocket, endereco = serverSocket.accept()
print(f"Conexão estabelecida com {endereco}")

receber = threading.Thread(target=receiveMessage,args=(conexaoSocket,))
enviar = threading.Thread(target=sendMessage,args=(conexaoSocket,))

receber.start()
enviar.start()

receber.join()
enviar.join()

conexaoSocket.close()
serverSocket.close()

