def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("El campo no puede estar vacio.")


def leer_flotante_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser mayor que cero.")
        except ValueError:
            print("Debe escribir un numero valido.")


def leer_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser mayor que cero.")
        except ValueError:
            print("Debe escribir un numero entero valido.")


def leer_entero_rango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"El valor debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Debe escribir un numero entero valido.")


def agregar_canciones(nombres, artistas, duraciones, popularidades):
    cantidad = leer_entero_positivo("Cuantas canciones desea agregar: ")

    for i in range(cantidad):
        print(f"Datos de la cancion {i + 1}")

        nombre = leer_texto("Nombre: ")
        artista = leer_texto("Artista: ")
        duracion = leer_flotante_positivo("Duracion en minutos: ")
        popularidad = leer_entero_rango("Popularidad (1-100): ", 1, 100)

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print(f"Se agregaron {cantidad} canciones.")


def mostrar_lista_canciones(nombres, artistas, duraciones, popularidades, indices):
    if len(indices) == 0:
        print("No se encontraron canciones.")
        return

    for posicion in indices:
        print(
            f"{posicion + 1}. {nombres[posicion]} | "
            f"{artistas[posicion]} | "
            f"Duracion: {duraciones[posicion]} | "
            f"Popularidad: {popularidades[posicion]}"
        )


def ver_reportes(nombres, artistas, duraciones, popularidades):
    if len(nombres) == 0:
        print("No hay canciones registradas.")
        return

    total = len(nombres)
    duracion_total = 0
    suma_popularidad = 0

    for i in range(total):
        duracion_total += duraciones[i]
        suma_popularidad += popularidades[i]

    mayor_popularidad = popularidades[0]
    menor_popularidad = popularidades[0]
    indice_mayor = 0
    indice_menor = 0

    for i in range(1, total):
        if popularidades[i] > mayor_popularidad:
            mayor_popularidad = popularidades[i]
            indice_mayor = i

        if popularidades[i] < menor_popularidad:
            menor_popularidad = popularidades[i]
            indice_menor = i

    promedio_popularidad = suma_popularidad / total

    print("REPORTES DE LA PLAYLIST")
    print(f"Numero total de canciones: {total}")
    print(f"Duracion total de la playlist: {duracion_total:.2f} minutos")
    print(
        f"Cancion mas popular: {nombres[indice_mayor]} de "
        f"{artistas[indice_mayor]} con {mayor_popularidad} de popularidad"
    )
    print(
        f"Cancion menos popular: {nombres[indice_menor]} de "
        f"{artistas[indice_menor]} con {menor_popularidad} de popularidad"
    )
    print(f"Promedio de popularidad: {promedio_popularidad:.2f}")


def buscar_canciones(nombres, artistas, duraciones, popularidades):
    if len(nombres) == 0:
        print("No hay canciones registradas.")
        return

    print("Buscar canciones")
    print("1. Por artista")
    print("2. Por rango de popularidad")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
        artista = leer_texto("Nombre del artista: ")
        indices = []

        for i in range(len(artistas)):
            if artistas[i].lower() == artista.lower():
                indices.append(i)

        mostrar_lista_canciones(nombres, artistas, duraciones, popularidades, indices)

    elif opcion == "2":
        while True:
            minimo = leer_entero_rango("Popularidad minima (1-100): ", 1, 100)
            maximo = leer_entero_rango("Popularidad maxima (1-100): ", 1, 100)

            if minimo <= maximo:
                break

            print("El valor minimo debe ser menor o igual que el valor maximo.")

        indices = []

        for i in range(len(popularidades)):
            if minimo <= popularidades[i] <= maximo:
                indices.append(i)

        mostrar_lista_canciones(nombres, artistas, duraciones, popularidades, indices)

    else:
        print("Opcion no valida.")


def playlist_recomendada(nombres, artistas, duraciones, popularidades):
    if len(nombres) == 0:
        print("No hay canciones registradas.")
        return

    suma_popularidad = 0

    for popularidad in popularidades:
        suma_popularidad += popularidad

    promedio = suma_popularidad / len(popularidades)
    indices = []

    for i in range(len(popularidades)):
        if popularidades[i] > promedio:
            indices.append(i)

    print("PLAYLIST RECOMENDADA")
    print(f"Promedio de popularidad: {promedio:.2f}")

    mostrar_lista_canciones(nombres, artistas, duraciones, popularidades, indices)


nombres = []
artistas = []
duraciones = []
popularidades = []

print("FESTIVAL PLAYLIST")

while True:
    print("1. Agregar canciones")
    print("2. Ver reportes")
    print("3. Buscar canciones")
    print("4. Playlist recomendada")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
        agregar_canciones(nombres, artistas, duraciones, popularidades)

    elif opcion == "2":
        ver_reportes(nombres, artistas, duraciones, popularidades)

    elif opcion == "3":
        buscar_canciones(nombres, artistas, duraciones, popularidades)

    elif opcion == "4":
        playlist_recomendada(nombres, artistas, duraciones, popularidades)

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opcion no valida.")