##definicion de atributos
class Bot:
    def __init__(self, nombre="", version=1.0, desarrollador="", activo=False):
        self._nombre = nombre
        self._version = version
        self._desarrollador = desarrollador
        self._activo = activo

    # metodos de acceso - encapsulamiento
    def obtener_nombre(self):
        return self._nombre

    def establecer_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def obtener_version(self):
        return self._version

    def establecer_version(self, nueva_version):
        self._version = nueva_version

    def obtener_desarrollador(self):
        return self._desarrollador

    def establecer_desarrollador(self, nuevo_desarrollador):
        self._desarrollador = nuevo_desarrollador

    def esta_activo(self):
        return self._activo

    def activar(self):
        self._activo = True

    def desactivar(self):
        self._activo = False

    def ejecutar_accion(self, accion):
        print(f"Bot ejecuta la acción: {accion}")
