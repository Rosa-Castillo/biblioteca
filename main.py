import catalogo
import socios
import prestamos

def menu():
    while True:
        print("\n=================================")
        print("  BIBLIOTECA DE BARRIO - MENÚ")
        print("=================================")
        print("1. Buscar libro")
        print("2. Dar de alta socio")
        print("3. Realizar préstamo")
        print("4. Devolver préstamo")
        print("5. Reservar libro prestado")
        print("6. Salir")
        
        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            titulo = input("Introduce el título a buscar: ")
            resultados = catalogo.buscar(titulo)
            if resultados:
                for libro in resultados:
                    print(f"\n[ID: {libro.id_libro}] Título: '{libro.titulo}' | Autor: {libro.autor}")
                    for ej in libro.ejemplares:
                        estado_str = ej.estado
                        if ej.reservado_por:
                            estado_str += f" (Reservado por {ej.reservado_por})"
                        print(f"   -> Ejemplar {ej.id_ejemplar} | Estado: {estado_str}")
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "2":
            nombre = input("Nombre completo del nuevo socio: ")
            nuevo = socios.dar_alta(nombre)
            print(f"Socio registrado correctamente. ID asignado: {nuevo.id_socio}")

        elif opcion == "3":
            id_socio = input("ID del socio (ej. S1): ")
            id_libro = input("ID del libro (ej. L1): ")
            exito, msg = prestamos.realizar_prestamo(id_socio, id_libro)
            print(f"\n[Resultado]: {msg}")

        elif opcion == "4":
            id_prestamo = input("ID del préstamo a devolver (ej. P1): ")
            exito, msg = prestamos.devolver_prestamo(id_prestamo)
            print(f"\n[Resultado]: {msg}")

        elif opcion == "5":
            id_socio = input("Tu ID de socio: ")
            id_libro = input("ID del libro a reservar: ")
            exito, msg = catalogo.reservar_ejemplar(id_libro, id_socio)
            print(f"\n[Resultado]: {msg}")

        elif opcion == "6":
            print("¡Gracias por usar la Biblioteca de Barrio!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()