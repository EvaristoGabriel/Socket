import socket
import time

SERVER_ADDRESS = ('localhost', 3333)

def cliente_udp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        while True:
            mensagem = str(input('Digite um número: '))
            sock.sendto(mensagem.encode('utf-8'), SERVER_ADDRESS)
            print(f"Enviado: {mensagem}")
            
            data, _ = sock.recvfrom(1024)
            resposta = data.decode('utf-8')
            print(f"Resposta do servidor: {resposta}")
            
            if resposta == "Buffer cheio":
                print("Servidor está cheio, parando envio.")
                break
            
            time.sleep(1)  
    finally:
        sock.sendto("STOP".encode('utf-8'), SERVER_ADDRESS)
        sock.close()
        print("Cliente encerrado.")

if __name__ == "__main__":
    cliente_udp()
