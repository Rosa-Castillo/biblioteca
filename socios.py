class Socio:
    def __init__(self, id_socio, nombre):
        self.id_socio = id_socio
        self.nombre = nombre
        self.sancionado = False
        self.libros_prestados = []  # Almacena los préstamos activos

# Base de datos simulada
_SOCIOS = [
    Socio("S1", "Ana Pérez"),
    Socio("S2", "Carlos Gómez")
]

# --- FUNCIONES PÚBLICAS DEL COMPONENTE ---

def dar_alta(nombre):
    """Registra un nuevo socio con ID automático."""
    nuevo_id = f"S{len(_SOCIOS) + 1}"
    nuevo_socio = Socio(nuevo_id, nombre)
    _SOCIOS.append(nuevo_socio)
    return nuevo_socio

def obtener(id_socio):
    """Obtiene la información de un socio por su ID."""
    for s in _SOCIOS:
        if s.id_socio == id_socio:
            return s
    return None

def puede_pedir_prestamo(id_socio):
    """Comprueba si un socio puede pedir un libro según las reglas."""
    socio = obtener(id_socio)
    if not socio:
        return False, "El socio no existe."
    if socio.sancionado:
        return False, "Acceso denegado: El socio está sancionado."
    if len(socio.libros_prestados) >= 2:
        return False, "Acceso denegado: Un socio no puede tener más de 2 libros simultáneamente."
    return True, "Socio autorizado."

def registrar_prestamo_socio(id_socio, id_prestamo):
    socio = obtener(id_socio)
    if socio:
        socio.libros_prestados.append(id_prestamo)

def registrar_devolucion_socio(id_socio, id_prestamo):
    socio = obtener(id_socio)
    if socio and id_prestamo in socio.libros_prestados:
        socio.libros_prestados.remove(id_prestamo)