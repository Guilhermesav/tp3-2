import socket,psutil,pickle

host = socket.gethostname()
port = 9995
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (host,port)
udp.bind(orig)
print(udp)
(msg,cliente) = udp.recvfrom(1024)
print(cliente,msg.decode('ascii'))

msg = [psutil.virtual_memory()[0],psutil.virtual_memory()[1]]

msg = pickle.dumps(msg)

udp.sendto(msg,(cliente))
    
#udp.close()


