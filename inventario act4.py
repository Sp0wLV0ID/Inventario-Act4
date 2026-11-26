
from abc import ABC, abstractmethod


# Va a definir los atributos y métodos comunes de todos los productos.
class Producto(ABC):

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    # Método común que reutilizan las clases derivadas.
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Precio: $", self.precio)
        print("Cantidad:", self.cantidad)

    # hace que las clases derivadas deban implementar el método mostrar_info() para poder crear objetos de ellas.
    @abstractmethod
    def mostrar_info(self):
        pass


# clases derivadas para los diferentes productos del inventario.
class Videojuego(Producto):

    def __init__(self, nombre, precio, cantidad, plataforma):
        super().__init__(nombre, precio, cantidad)
        self.plataforma = plataforma

    def mostrar_info(self):
        self.mostrar_datos()
        print("Plataforma:", self.plataforma)


class Computadora(Producto):

    def __init__(self, nombre, precio, cantidad, procesador):
        super().__init__(nombre, precio, cantidad)
        self.procesador = procesador

    def mostrar_info(self):
        self.mostrar_datos()
        print("Procesador:", self.procesador)


class Consola(Producto):

    def __init__(self, nombre, precio, cantidad, marca):
        super().__init__(nombre, precio, cantidad)
        self.marca = marca

    def mostrar_info(self):
        self.mostrar_datos()
        print("Marca:", self.marca)


class Control(Producto):

    def __init__(self, nombre, precio, cantidad, conexion):
        super().__init__(nombre, precio, cantidad)
        self.conexion = conexion

    def mostrar_info(self):
        self.mostrar_datos()
        print("Conexión:", self.conexion)


class DiscoDuro(Producto):

    def __init__(self, nombre, precio, cantidad, capacidad):
        super().__init__(nombre, precio, cantidad)
        self.capacidad = capacidad

    def mostrar_info(self):
        self.mostrar_datos()
        print("Capacidad:", self.capacidad)


# control del inventario de los productos y sus metodos.
class Inventario:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")

        # Aplicacion del polimorfismo.
        for producto in self.productos:
            producto.mostrar_info()
            print("------------------------------")

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)

        if producto:
            self.productos.remove(producto)
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_cantidad(self, nombre, cantidad):
        producto = self.buscar_producto(nombre)

        if producto:
            producto.cantidad = cantidad
            print("Cantidad actualizada.")
        else:
            print("Producto no encontrado.")


# Programa principal
def main():

    inventario = Inventario()

    # Menú principal
    while True:
        print("\n=== 🎮 Tienda de videojuegos ===")
        print(" 1. Agregar producto ➕")
        print(" 2. Ver inventario 📋")
        print(" 3. Buscar producto 🔍")
        print(" 4. Eliminar producto 🗑️")
        print(" 5. Actualizar cantidad 🔄")
        print(" 6. Salir 👋")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            print("\n=== 📦 Tipos de productos ===")
            print(" 1. Videojuego 🎮")
            print(" 2. Computadora 💻")
            print(" 3. Consola 🕹️")
            print(" 4. Control 🎯")
            print(" 5. Disco duro 💾")

            tipo = input("\nSelecciona el tipo de producto: ")

            if tipo not in ["1", "2", "3", "4", "5"]:
                print("Tipo de producto no válido.")
                continue

            nombre = input("Nombre: ")

            if inventario.buscar_producto(nombre):
                print("El producto ya está registrado.")
                continue

            # Validamos que los datos sean números.
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("Introduce valores numéricos válidos.")
                continue

            if precio < 0 or cantidad < 0:
                print("No se permiten valores negativos.")
                continue

            # se crea un objeto segun el tipo de producto.
            if tipo == "1":
                plataforma = input("Plataforma: ")
                producto = Videojuego(nombre, precio, cantidad, plataforma)

            elif tipo == "2":
                procesador = input("Procesador: ")
                producto = Computadora(nombre, precio, cantidad, procesador)

            elif tipo == "3":
                marca = input("Marca: ")
                producto = Consola(nombre, precio, cantidad, marca)

            elif tipo == "4":
                conexion = input("Conexión: ")
                producto = Control(nombre, precio, cantidad, conexion)

            else:
                capacidad = input("Capacidad: ")
                producto = DiscoDuro(nombre, precio, cantidad, capacidad)

            inventario.agregar_producto(producto)

        # 📋 Mostrar todos los productos
        elif opcion == "2":
            inventario.mostrar_inventario()

        # 🔍 Buscar un producto
        elif opcion == "3":
            producto = inventario.buscar_producto(input("Nombre: "))

            if producto:
                producto.mostrar_info()
            else:
                print("Producto no encontrado.")

        # 🗑️ Eliminar un producto
        elif opcion == "4":
            inventario.eliminar_producto(input("Nombre: "))

        # 🔢 Actualizar la cantidad
        elif opcion == "5":
            nombre = input("Nombre: ")

            try:
                cantidad = int(input("Nueva cantidad: "))
            except ValueError:
                print("Introduce una cantidad válida.")
                continue

            if cantidad < 0:
                print("No se permiten cantidades negativas.")
            else:
                inventario.actualizar_cantidad(nombre, cantidad)

        # 👋 Salir del programa
        elif opcion == "6":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opción no válida.")


main()


