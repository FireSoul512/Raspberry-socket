import socket
from socket import gethostbyname, create_connection, error
import time
from servo import SERVO
from peso import PESO

def comprobarConexionUno():
    ciclo = True
    while ciclo:
        try:
            gethostbyname("google.com")
            conexion = create_connection(("google.com", 80), 1)
            conexion.close()
            ciclo = False
            return "Hay conexión a internet..."
        except error:
            time.sleep(5)

serv = SERVO()
serv.start()

time.sleep(30)
conexionUno = comprobarConexionUno()
print(conexionUno)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( ('192.168.1.71',7080) )
s.listen(5)
ciclo = True
print('Para cerrar el server el cliente tiene que introducir SALIR')

try:
    while ciclo:
        conexion, addr = s.accept()
        print("Nueva conexion",addr)
        msg = conexion.recv(1024)
        if msg.decode("utf-8") == "SERVO":
            serv = SERVO()
            serv.mover()
            pes = PESO()
            mensaje = pes.obtener()
            conexion.send(bytes(str(mensaje),'utf-8'))

        elif msg.decode("utf-8") == "PESO":
            pes = PESO()
            mensaje = pes.obtener()
            conexion.send(bytes(str(mensaje),'utf-8'))

        else:
            mensaje = "Te manda saludos la rasp"
            conexion.send(bytes(mensaje,'utf-8'))
            
        conexion.close()

    print('Adios bro XD')
    s.close()

except (KeyboardInterrupt):
    print()
    print('Adios')

finally:
    s.close()
