from socket import *
import threading

# configurando o servidor
serverName = 'localhost'
serverPort = 3333


clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def receber_mensagens():
    while True:
        try:
            mensagem = clientSocket.recv(2048).decode()
            if mensagem:
                print(f"Servidor: {mensagem}")
            else:
                break
        except:
            print("Conexão encerrada.")
            break

# Função para enviar mensagens ao servidor
def enviar_mensagens():
    while True:
        mensagem = input("Cliente: ")
        clientSocket.send(mensagem.encode())

# Criando threads para envio e recepção de mensagens
receber = threading.Thread(target=receber_mensagens)
enviar = threading.Thread(target=enviar_mensagens)

receber.start()
enviar.start()

receber.join()
enviar.join()

clientSocket.close()
