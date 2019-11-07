import socket
import psutil, pickle

  
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


  
host = socket.gethostname()
porta = 8881
socket_servidor.bind((host, porta))
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)

while True:
    (socket_cliente,addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    nome_arq = msg.decode('ascii')
    if os.path.isfile(nome_arq):
        # Envia primeiro o tamanho
        tamanho = os.stat(nome_arq).st_size
        socket_cliente.send(str(tamanho).encode('ascii'))
        # Abre o arquivo no modo leitura de bytes
        arq = open(nome_arq, 'rb')
        # Envia os dados
        bytes = arq.read(4096)
    while bytes:
            socket_cliente.send(bytes)
            bytes = arq.read(4096)
        # Fecha o arquivo
        arq.close()
        else:
        print("Não encontrou o arquivo")
        # tamanho é -1 para indicar que não achou arquivo
        socket_cliente.send('-1'.encode('ascii'))
        
      socket_cliente.send(nomes)
      socket_cliente.close()