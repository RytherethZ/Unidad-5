class Cine:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.asientos = [["L"] * columnas for f in range(filas)]

    def existe(self, fila, columna):
        return 0 <= fila < self.filas and 0 <= columna < self.columnas

    def reservar(self, fila, columna):
        if not self.existe(fila, columna):
            print("El asiento no existe.")
            return False

        if self.asientos[fila][columna] == "X":
            print("El asiento ya esta ocupado.")
            return False

        self.asientos[fila][columna] = "X"
        print(f"Asiento reservado en fila {fila}, columna {columna}.")
        return True

    def liberar(self, fila, columna):
        if not self.existe(fila, columna):
            print("El asiento no existe.")
            return False

        if self.asientos[fila][columna] == "L":
            print("El asiento ya esta libre.")
            return False

        self.asientos[fila][columna] = "L"
        print(f"Asiento liberado en fila {fila}, columna {columna}.")
        return True

    def contar(self):
        libres = 0
        ocupados = 0

        for fila in self.asientos:
            for asiento in fila:
                if asiento == "L":
                    libres += 1
                else:
                    ocupados += 1

        return libres, ocupados

    def mostrar(self):
        print("ESTADO DE LA SALA")

        print("    ", end="")
        for c in range(self.columnas):
            print(f"{c} ", end="")
        print()

        for f in range(self.filas):
            print(f"{f}: ", end="")
            for c in range(self.columnas):
                print(f"{self.asientos[f][c]} ", end="")
            print()

        print()


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe escribir un numero entero.")


print("SISTEMA DE ASIENTOS DE CINE")

filas = leer_entero("Numero de filas: ")
while filas <= 0:
    print("La cantidad de filas debe ser mayor que cero.")
    filas = leer_entero("Numero de filas: ")

columnas = leer_entero("Numero de columnas: ")
while columnas <= 0:
    print("La cantidad de columnas debe ser mayor que cero.")
    columnas = leer_entero("Numero de columnas: ")

cine = Cine(filas, columnas)

print("Sala creada.")
cine.mostrar()
print("Recuerde: la primera fila y la primera columna son 0.")

while True:
    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
        cine.mostrar()

    elif opcion == "2":
        fila = leer_entero("Fila del asiento: ")
        columna = leer_entero("Columna del asiento: ")
        cine.reservar(fila, columna)

    elif opcion == "3":
        fila = leer_entero("Fila del asiento: ")
        columna = leer_entero("Columna del asiento: ")
        cine.liberar(fila, columna)

    elif opcion == "4":
        libres, ocupados = cine.contar()
        print(f"Asientos libres: {libres}")
        print(f"Asientos ocupados: {ocupados}")

    elif opcion == "5":
        print("Saliendo del sistema.")
        break

    else:
        print("Opcion no valida.")