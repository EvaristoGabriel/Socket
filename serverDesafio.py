import socket
import threading
import time
import random


BUFFER_SIZE = 10
TTL = 30  
SERVER_PORT = 3333

buffer = []
ttl_map = {}
lock = threading.Lock()
running = True

def gerenciar_ttl():
    global buffer, ttl_map, running
    while running:
        current_time = time.time()
        with lock:
            expirados = [item for item in buffer if ttl_map[item] < current_time]
            for item in expirados:
                buffer.remove(item)
                del ttl_map[item]
                print(f"Elemento {item} removido por expiração de TTL")
        time.sleep(1)

def aplicar_politicas_de_substituicao():
    global buffer, ttl_map
    if buffer:
        # FIFO: Remove o primeiro elemento
        removido_fifo = buffer.pop(0)
        del ttl_map[removido_fifo]
        print(f"Elemento {removido_fifo} removido pela política FIFO")
    if buffer:
        # Substituição aleatória: Remove um elemento aleatório
        removido_random = random.choice(buffer)
        buffer.remove(removido_random)
        del ttl_map[removido_random]
        print(f"Elemento {removido_random} removido pela política aleatória")

def servidor_udp():
    global buffer, ttl_map, running

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', SERVER_PORT))

    threading.Thread(target=gerenciar_ttl, daemon=True).start()

    while running:
        try:
            data, client_address = sock.recvfrom(1024)
            mensagem = data.decode('utf-8')
            
            if mensagem == "STOP":
                sock.sendto("Encerrando conexão".encode('utf-8'), client_address)
                break
            
            with lock:
                if len(buffer) >= BUFFER_SIZE:
                    aplicar_politicas_de_substituicao()
                    sock.sendto("Buffer cheio".encode('utf-8'), client_address)
                else:
                    numero = int(mensagem)
                    buffer.append(numero)
                    ttl_map[numero] = time.time() + TTL
                    sock.sendto("ACK".encode('utf-8'), client_address)
            
            print(f"Buffer atual: {buffer}")
        
        except Exception as e:
            print(f"Erro: {e}")
    
    running = False
    sock.close()
    print("Servidor encerrado.")

if __name__ == "__main__":
    servidor_udp()
