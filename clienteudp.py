#UDP CLIENT:

import socket,pickle

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = 'olar'
msg = msg.encode('ascii')

udp.sendto(msg,("10.2.13.76", 9995))

(msg,servidor) = udp.recvfrom(1024)

print(servidor, pickle.loads(msg))

print(udp)

#udp.close()
  
  