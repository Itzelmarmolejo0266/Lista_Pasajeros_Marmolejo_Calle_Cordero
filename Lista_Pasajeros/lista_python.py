from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Las mismas operaciones usando los métodos del list de Python."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):
        if self.buscar(pasajero.numero) != -1:         # mismo criterio que Lista 1
            print(f"  ⚠ Ya existe el pasajero #{pasajero.numero}")
            return False
        self.pasajeros.append(pasajero)
        return True

    def listar(self):
        if not self.pasajeros:
            print("  (lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"  [{i}] {p}")

    # ---------------- tabla 3.2 ----------------
    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            print(f"  ⚠ Posición inválida (use 0 a {len(self.pasajeros)})")
            return False
        if self.buscar(pasajero.numero) != -1:
            print(f"  ⚠ Ya existe el pasajero #{pasajero.numero}")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    def buscar(self, numero):
        posiciones = [i for i, p in enumerate(self.pasajeros) if p.numero == numero]
        return posiciones[0] if posiciones else -1

    def buscar_binaria(self, numero):                  # requiere lista ordenada
        numeros = [p.numero for p in self.pasajeros]
        i = bisect_left(numeros, numero)
        if i < len(numeros) and numeros[i] == numero:
            return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.pasajeros[pos].destino = nuevo_destino
        self.pasajeros[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            return None
        return self.pasajeros.pop(posicion)

    def eliminar_por_valor(self, numero):
        antes = len(self.pasajeros)
        self.pasajeros = [p for p in self.pasajeros if p.numero != numero]
        return len(self.pasajeros) < antes

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva = ListaPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):           # solo Lista 2
        return [p for p in self.pasajeros if p.destino.lower() == destino.lower()]

    def mayores_de_edad(self):                        # solo Lista 2
        return [p for p in self.pasajeros if p.es_mayor_de_edad()]
