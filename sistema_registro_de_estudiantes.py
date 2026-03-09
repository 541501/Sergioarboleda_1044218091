# Programa: Sistema de Registro de Estudiantes
# Este programa registra información de 5 estudiantes, valida los datos,
# y muestra estadísticas al final.

# Lista para almacenar los estudiantes (cada uno como un diccionario)
estudiantes = []

# Bucle para registrar 5 estudiantes
for i in range(5):
    print(f"\nRegistro del estudiante {i+1}:")

    # Pedir y validar nombre
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre:  # Verificar que no esté vacío
            break
        else:
            print("El nombre no puede estar vacío. Intente de nuevo.")

    # Pedir y validar edad
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante (5-100): "))
            if 5 <= edad <= 100:
                break
            else:
                print("La edad debe estar entre 5 y 100. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número entero para la edad.")

    # Pedir y validar calificación
    while True:
        try:
            calificacion = float(input("Ingrese la calificación del estudiante (0-5): "))
            if 0 <= calificacion <= 5:
                break
            else:
                print("La calificación debe estar entre 0 y 5. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido para la calificación.")

    # Guardar la información del estudiante
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "calificacion": calificacion
    }
    estudiantes.append(estudiante)

# Calcular estadísticas
# Inicializar variables para acumuladores y extremos
suma_calificaciones = 0
max_calificacion = -1
min_calificacion = 6
estudiante_max = ""
estudiante_min = ""

for estudiante in estudiantes:
    cal = estudiante["calificacion"]
    suma_calificaciones += cal  # Acumulador para la suma

    if cal > max_calificacion:
        max_calificacion = cal
        estudiante_max = estudiante["nombre"]

    if cal < min_calificacion:
        min_calificacion = cal
        estudiante_min = estudiante["nombre"]

# Calcular promedio
promedio = suma_calificaciones / 5

# Mostrar resultados
print("\n--- Estadísticas ---")
print(f"Estudiante con la calificación más alta: {estudiante_max} ({max_calificacion})")
print(f"Estudiante con la calificación más baja: {estudiante_min} ({min_calificacion})")
print(f"Calificación promedio de todos los estudiantes: {promedio:.2f}")