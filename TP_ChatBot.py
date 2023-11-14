#importar clases
from inspect import isclass
from multiprocessing.connection import Client
import os
from operator import isub
from re import S
from Agente import Agente
from Cliente import Cliente
from Usuario import Usuario



## Usuarios Hardcodeados

cliente1 = Cliente(nombre="John", apellido="Doe", correo="john@example.com", edad=25, ciudad="New York", codCliente=111222)
cliente2 = Cliente(nombre="Jane", apellido="Doe", correo="jane@example.com", edad=30, ciudad="Los Angeles", codCliente=111333)
cliente3 = Cliente(nombre="Alice", apellido="Smith", correo="alice@example.com", edad=22, ciudad="Chicago", codCliente=111444)
cliente4 = Cliente(nombre="Eva", apellido="Johnson", correo="eva@example.com", edad=28, ciudad="Miami", codCliente=111555)
cliente5 = Cliente(nombre="David", apellido="Brown", correo="david@example.com", edad=35, ciudad="Houston", codCliente=111666)
cliente6 = Cliente(nombre="Sophia", apellido="Miller", correo="sophia@example.com", edad=26, ciudad="San Francisco", codCliente=111777)
cliente7 = Cliente(nombre="Daniel", apellido="Wilson", correo="daniel@example.com", edad=31, ciudad="Seattle", codCliente=111888)
cliente8 = Cliente(nombre="Olivia", apellido="Moore", correo="olivia@example.com", edad=24, ciudad="Denver", codCliente=111999)
cliente9 = Cliente(nombre="Matthew", apellido="Taylor", correo="matthew@example.com", edad=29, ciudad="Dallas", codCliente=111000)

Lista_usuarios = [cliente1, cliente2, cliente3, cliente4, cliente5, cliente6, cliente7, cliente8, cliente9]

actualClient = Cliente(nombre="", apellido="", correo="", edad=0, ciudad="", codCliente=0)

##
def limpiar():
    os.system("cls")

## menu principal

print("Hola, Bienvenido al 'Compu Hiper Mega Red'. Ya sos cliente? ")
print("Si") 
print("No")

isUser = input() 


if isUser == 'Si' or 'si':
    limpiar()

    isDocumento = input("Por favor ingrese su numero de documento : \n")
    print(isDocumento)
    
    for isClient in Lista_usuarios:
        if isDocumento == isClient._codCliente:
            actualClient = isClient
            print(f"Hola: {actualClient._nombre}")
            break            
       
    if actualClient:
        print(f"Hola: {actualClient._nombre}") ##no imprime el usuario encontrado, alguien puede arreglarlo?
    else:
        print("No se encontro un cliente asociado al numero de documento")

        
    # print("\n Selecciona la opcion deseada \n" )    

    # print("1. Internet")
    # print("2. Telefonia")
    # print("3. TV Cable")
    # print("4. Consultas Administrativas")
    # print("5. Baja de Servicio")
    # print("6. Comunicarse con un Agente")

else:
    print("\n Selecciona la opcion deseada \n" )
    
    print("7. Contratar un Servicio")
    
