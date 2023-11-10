class Usuario(object):

##Superclase Usuario
#definicion de atributos
 def __init__(self, nombre="", apellido="", correo="", edad=0, ciudad=""):
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._edad = edad
        self._ciudad = ciudad

 # metodos de acceso - encapsulamiento
def obtener_nombre(self):
    return self._nombre

def establecer_nombre(self, nuevo_nombre):
    self._nombre = nuevo_nombre

def obtener_apellido(self):
    return self._apellido

def establecer_apellido(self, nuevo_apellido):
    self._apellido = nuevo_apellido

def obtener_correo(self):
    return self._correo

def establecer_correo(self, nuevo_correo):
    self._correo = nuevo_correo

def obtener_edad(self):
    return self._edad

def establecer_edad(self, nueva_edad):
    self._edad = nueva_edad

def obtener_ciudad(self):
    return self._ciudad

def establecer_ciudad(self, nueva_ciudad):
    self._ciudad = nueva_ciudad