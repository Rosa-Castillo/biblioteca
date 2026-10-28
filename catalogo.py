from datetime import datetime

class Ejemplar:
    def __init__(self, id_ejemplar, id_libro):
        self.id_ejemplar = id_ejemplar
        self.id_libro = id_libro
        self.estado = "disponible"  # Puede ser: disponible, prestado, reservado
        self.reservado_por = None

class Libro:
    def __init__(self, id_libro, titulo, autor, num_ejemplares=2):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        # Creamos los ejemplares asociados al libro
        self.ejemplares = [Ejemplar(f"{id_libro}-E{i+1}", id_libro) for i in range(num_ejemplares)]

# Datos simulados en memoria
_CATALOGO = [
    Libro("L1", "Cien años de soledad", "Gabriel García Márquez", 2),
    Libro("L2", "1984", "George Orwell", 2)
]

# --- FUNCIONES PÚBLICAS DEL COMPONENTE ---

def buscar(titulo):
    """Busca libros cuyo título contenga el texto introducido."""
    titulo_lower = titulo.lower()
    resultados = []
    for libro in _CATALOGO:
        if titulo_lower in libro.titulo.lower():
            resultados.append(libro)
    return resultados

def obtener(id_libro):
    """Obtiene un libro por su ID."""
    for libro in _CATALOGO:
        if libro.id_libro == id_libro:
            return libro
    return None

def obtener_ejemplar_disponible(id_libro):
    """Devuelve el primer ejemplar disponible de un libro."""
    libro = obtener(id_libro)
    if libro:
        for ej in libro.ejemplares:
            if ej.estado == "disponible":
                return ej
    return None

def marcar_prestado(id_ejemplar):
    """Cambia el estado de un ejemplar a prestado."""
    for libro in _CATALOGO:
        for ej in libro.ejemplares:
            if ej.id_ejemplar == id_ejemplar:
                ej.estado = "prestado"
                ej.reservado_por = None
                return True
    return False

def marcar_disponible(id_ejemplar):
    """Devuelve un ejemplar a estado disponible."""
    for libro in _CATALOGO:
        for ej in libro.ejemplares:
            if ej.id_ejemplar == id_ejemplar:
                ej.estado = "disponible"
                return True
    return False

def reservar_ejemplar(id_libro, id_socio):
    """Permite reservar un ejemplar si están todos prestados."""
    libro = obtener(id_libro)
    if not libro:
        return False, "El libro no existe en el catálogo."
    for ej in libro.ejemplares:
        if ej.estado == "prestado":
            ej.estado = "reservado"
            ej.reservado_por = id_socio
            return True, f"Ejemplar {ej.id_ejemplar} reservado con éxito para el socio {id_socio}."
    return False, "No es posible reservar: hay ejemplares disponibles para préstamo inmediato."