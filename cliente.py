import socket


ciclo = True
while ciclo:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect( ('192.168.1.71',7080) )
    mensaje = input('Introduce el mensaje >>  ')
    print()
    s.send(bytes(mensaje, "utf-8"))
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
    s.close()
    if mensaje == "SALIR":
        ciclo = False
print()
print("ADIOS")