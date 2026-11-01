from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()


# ------------------------- funciones de apoyo -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def cargar_datos_prueba(lista):
    lista.añadir(Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"))
    lista.añadir(Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"))
    lista.añadir(Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"))
    lista.añadir(Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"))
    lista.añadir(Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"))
    print("  ✓ Datos de prueba cargados")


def mostrar_opciones(titulo, extras=False):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir           2. Listar            3. Insertar en posición")
    print(" 4. Buscar (lineal)  5. Buscar (binaria)  6. Modificar")
    print(" 7. Eliminar por posición                 8. Eliminar por número")
    print(" 9. Ordenar asc     10. Ordenar desc     11. Reversar")
    print("12. Copiar          13. Longitud")
    if extras:
        print("14. Filtrar por destino                  15. Mayores de edad")
    print(" C. Cargar datos de prueba                0. Volver")


def mostrar_encontrado(lista, pos):
    """Muestra el resultado de una búsqueda (pos = posición o -1)."""
    if pos == -1:
        print("  No existe")
    else:
        nombre = lista.datos[pos].nombre if hasattr(lista, "datos") else lista.pasajeros[pos].nombre
        print(f"  Encontrado en [{pos}]: {nombre}")


# --------- operaciones comunes (3 a 13): LEER -> LLAMAR -> MOSTRAR ---------
# Las dos listas tienen los mismos métodos, así que un solo bloque sirve a ambos menús.
def ejecutar_operacion(lista, op):
    """Devuelve True si la opción era una de las comunes (1 a 13 o C)."""
    if op == "1":
        pasajero = leer_pasajero()                          # 1. LEER
        if lista.añadir(pasajero):                          # 2. LLAMAR
            print("  ✓ Pasajero añadido")                   # 3. MOSTRAR

    elif op == "2":
        lista.listar()

    elif op == "3":
        pos = leer_entero("  Posición donde insertar: ")
        pasajero = leer_pasajero()
        if lista.insertar(pos, pasajero):
            print(f"  ✓ Insertado en [{pos}]")
        # si falla, insertar ya imprimió el motivo

    elif op == "4":
        numero = leer_entero("  N.º a buscar: ")
        mostrar_encontrado(lista, lista.buscar(numero))

    elif op == "5":
        print("  (la lista debe estar ordenada: use la opción 9 antes)")
        numero = leer_entero("  N.º a buscar: ")
        mostrar_encontrado(lista, lista.buscar_binaria(numero))

    elif op == "6":
        numero = leer_entero("  N.º del pasajero a modificar: ")
        destino = input("  Nuevo destino: ").strip()
        asiento = input("  Nuevo asiento: ").strip().upper()
        if lista.modificar(numero, destino, asiento):
            print("  ✓ Pasajero modificado")
        else:
            print("  No existe")

    elif op == "7":
        pos = leer_entero("  Posición a eliminar: ")
        eliminado = lista.eliminar_por_posicion(pos)
        if eliminado is None:
            print("  ⚠ Posición inválida")
        else:
            print(f"  Eliminado: {eliminado.nombre}; quedan {lista.longitud()}")

    elif op == "8":
        numero = leer_entero("  N.º a eliminar: ")
        if lista.eliminar_por_valor(numero):
            print(f"  ✓ Pasajero #{numero} eliminado")
        else:
            print("  No existe")

    elif op == "9":
        lista.ordenar_asc()
        print("  ✓ Ordenada de menor a mayor")
        lista.listar()

    elif op == "10":
        lista.ordenar_desc()
        print("  ✓ Ordenada de mayor a menor")
        lista.listar()

    elif op == "11":
        lista.reversar()
        print("  ✓ Lista reversada")
        lista.listar()

    elif op == "12":
        copia = lista.copiar()
        print("  Copia:")
        copia.listar()
        copia.reversar()                                    # demostración: la copia es independiente
        print("  Copia reversada:")
        copia.listar()
        print("  Original (no cambia):")
        lista.listar()

    elif op == "13":
        print(f"  Hay {lista.longitud()} pasajero(s)")

    elif op == "C":
        cargar_datos_prueba(lista)

    else:
        return False
    return True


# ---------------------- MENÚ 1 · MiLista ----------------------
def menu_lista1():
    while True:
        mostrar_opciones("MENÚ 1 · MiLista")
        op = input("Opción: ").strip().upper()
        if op == "0":
            break
        if not ejecutar_operacion(lista1, op):
            print("  Opción no válida")


# ---------------------- MENÚ 2 · list de Python ----------------------
def menu_lista2():
    while True:
        mostrar_opciones("MENÚ 2 · list de Python", extras=True)
        op = input("Opción: ").strip().upper()
        if op == "0":
            break
        if ejecutar_operacion(lista2, op):
            continue
        if op == "14":                                      # solo Lista 2
            destino = input("  Destino: ").strip()
            resultado = lista2.filtrar_por_destino(destino)
            if not resultado:
                print("  (ningún pasajero va a ese destino)")
            for p in resultado:
                print(f"  {p}")
        elif op == "15":
            resultado = lista2.mayores_de_edad()
            if not resultado:
                print("  (no hay mayores de edad)")
            for p in resultado:
                print(f"  {p}")
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    while True:
        print("\n===== TAREA LISTAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · MiLista")
        print("2. Menú 2 · list de Python")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
