import socket

HOST = socket.gethostname() # Endereco IP do Servidor
PORT = 5000                 # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
#print(udp)
print('Esperando receber na porta', PORT, '...')
(msg, cliente) = udp.recvfrom(1024)
print(cliente, msg.decode('ascii'))
udp.close()
input('Pressione qualquer tecla para sair...')