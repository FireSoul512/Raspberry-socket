import socket
from servo import SERVO

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( ('192.168.1.71',7080) )
s.listen(5)
ciclo = True
print('Para cerrar el server el cliente tiene que introducir SALIR')

while ciclo:
    conexion, addr = s.accept()
    print("Nueva conexion",addr)
    print(addr)
    conexion.send(bytes("Hola como estas", "utf-8"))
    msg = conexion.recv(1024)
    conexion.close()
    if msg.decode("utf-8") == "SALIR":
        ciclo = False
    if msg.decode("utf-8") == "SERVO":
        serv = SERVO()
        serv.mover()
        print("Entra al servo XD")

print('Adios bro XD')