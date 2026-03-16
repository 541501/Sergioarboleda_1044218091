import re

def validar_cedula(cedula):
    return cedula.isdigit() and 8 <= len(cedula) <= 10


def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None


def validar_calificaciones(calificaciones):
    for c in calificaciones:
        if c < 0 or c > 5:
            return False
    return True


def calcular_promedio(calificaciones):
    return round(sum(calificaciones) / len(calificaciones), 2)


def clasificar_desempeño(promedio):
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Satisfactorio"
    else:
        return "Necesita mejorar"


def crear_estudiante(cedula, nombre, email, calificaciones):
    if not validar_cedula(cedula):
        return None
    if not validar_email(email):
        return None
    if not validar_calificaciones(calificaciones):
        return None

    promedio = calcular_promedio(calificaciones)

    return {
        "cedula": cedula,
        "nombre": nombre,
        "email": email,
        "promedio": promedio
    }


def listar_estudiantes(lista_estudiantes):
    print("\nCédula    | Nombre           | Promedio | Desempeño")
    print("-" * 50)

    for e in lista_estudiantes:
        desempeño = clasificar_desempeño(e["promedio"])
        print(f'{e["cedula"]:<9} | {e["nombre"]:<15} | {e["promedio"]:<8} | {desempeño}')


def buscar_estudiante(lista_estudiantes, cedula):
    for e in lista_estudiantes:
        if e["cedula"] == cedula:
            desempeño = clasificar_desempeño(e["promedio"])
            print(f'{e["nombre"]} | Promedio: {e["promedio"]} | Desempeño: {desempeño}')
            return
    print("Estudiante no encontrado.")


def main():
    estudiantes = []

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Buscar estudiante por cédula")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            email = input("Email: ")
            notas = input("Calificaciones (separadas por coma): ")

            try:
                calificaciones = [float(n) for n in notas.split(",")]
            except:
                print("Error en las calificaciones.")
                continue

            estudiante = crear_estudiante(cedula, nombre, email, calificaciones)

            if estudiante:
                estudiantes.append(estudiante)
                desempeño = clasificar_desempeño(estudiante["promedio"])
                print(f'Estudiante agregado exitosamente. Promedio: {estudiante["promedio"]} | Desempeño: {desempeño}')
            else:
                print("Datos inválidos. No se pudo crear el estudiante.")

        elif opcion == "2":
            if estudiantes:
                listar_estudiantes(estudiantes)
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "3":
            cedula = input("Cédula a buscar: ")
            buscar_estudiante(estudiantes, cedula)

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


main()