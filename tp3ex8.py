#UDP CLIENT:

import socket,pickle

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = 'ola, Favor enviar a quantidade de memoria total e disponivel no disco principal'
msg = msg.encode('ascii')
cliente = socket.gethostname()
ip = socket.gethostbyname(cliente)
udp.sendto(msg,(ip, 9991))

(msg,servidor) = udp.recvfrom(4096)

print(servidor, pickle.loads(msg))

print(udp)

  
  