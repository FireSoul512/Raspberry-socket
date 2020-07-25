import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( ('localhost',7080) )

mensaje = input('Introduce el mensaje >>  ')
s.send(bytes(mensaje, "utf-8"))
msg = s.recv(1024)
print(msg.decode("utf-8"))
s.close()