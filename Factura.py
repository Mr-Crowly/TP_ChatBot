
#definicion de atributos
class Factura:
    def __init__(self, numero="", fecha="", cliente="", productos=None, total=0.0):
        self._numero = numero
        self._fecha = fecha
        self._cliente = cliente
        self._productos = productos or []  # lista de productos de la factura, ej internet, tv, paquetes, etc.
        self._total = total

    # metodos de acceso - encapsulamiento
    def obtener_numero(self):
        return self._numero

    def establecer_numero(self, nuevo_numero):
        self._numero = nuevo_numero

    def obtener_fecha(self):
        return self._fecha

    def establecer_fecha(self, nueva_fecha):
        self._fecha = nueva_fecha

    def obtener_cliente(self):
        return self._cliente

    def establecer_cliente(self, nuevo_cliente):
        self._cliente = nuevo_cliente

    def obtener_productos(self):
        return self._productos

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def obtener_total(self):
        return self._total

    def calcular_total(self):
        self._total = sum(producto.precio for producto in self._productos)


