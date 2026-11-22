def leer_entero(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            numero = int(valor)
            if numero > 0:
                return numero
        print("Ingrese un número entero mayor que 0.")


def leer_calificacion(estudiante, materia):
    while True:
        valor = input(f"Calificación del {estudiante} en la {materia}: ").strip()
        try:
            calificacion = float(valor)
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if 0 <= calificacion <= 100:
            return calificacion

        print("La calificación debe estar entre 0 y 100.")


estudiantes = leer_entero("¿Cuántos estudiantes tiene el grupo? ")
materias = leer_entero("¿Cuántas materias tiene el grupo? ")

calificaciones = []

for i in range(estudiantes):
    fila = []
    for j in range(materias):
        calificacion = leer_calificacion(f"estudiante {i + 1}", f"materia {j + 1}")
        fila.append(calificacion)
    calificaciones.append(fila)

mayor = calificaciones[0][0]
menor = calificaciones[0][0]

for fila in calificaciones:
    for valor in fila:
        if valor > mayor:
            mayor = valor
        if valor < menor:
            menor = valor

print()
print("RESULTADOS")
print("-" * 45)

for i in range(estudiantes):
    promedio = sum(calificaciones[i]) / materias
    print(f"Promedio del estudiante {i + 1}: {promedio:.2f}")

print()

for j in range(materias):
    suma = 0
    for i in range(estudiantes):
        suma += calificaciones[i][j]
    promedio = suma / estudiantes
    print(f"Promedio de la materia {j + 1}: {promedio:.2f}")

print()
print(f"Calificación más alta: {mayor:.2f}")
print(f"Calificación más baja: {menor:.2f}")