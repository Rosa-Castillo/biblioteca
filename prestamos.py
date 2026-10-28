from datetime import datetime, timedelta
import catalogo
import socios

class Prestamo:
    def __init__(self, id_prestamo, id_socio, id_ejemplar):
        self.id_prestamo = id_prestamo
        self.id_socio = id_socio
        self.id_ejemplar = id_ejemplar
        self.fecha_prestamo = datetime.now()
        self.fecha_caducidad = self.fecha_prestamo + timedelta(days=7) # Caduca a los 7 días
        self.devuelto = False

_PRESTAMOS = []

# --- FUNCIONES PÚBLICAS DEL COMPONENTE ---

def realizar_prestamo(id_socio, id_libro):
    # 1. Consultar permiso al módulo de socios
    permitido, mensaje = socios.puede_pedir_prestamo(id_socio)
    if not permitido:
        return False, mensaje

    # 2. Consultar ejemplar disponible al módulo de catálogo
    ejemplar = catalogo.obtener_ejemplar_disponible(id_libro)
    if not ejemplar:
        return False, "No hay ejemplares disponibles de este libro. Puedes intentar reservarlo."

    # 3. Marcar ejemplar como prestado en el catálogo
    catalogo.marcar_prestado(ejemplar.id_ejemplar)

    # 4. Crear registro de préstamo
    nuevo_id_p = f"P{len(_PRESTAMOS) + 1}"
    prestamo = Prestamo(nuevo_id_p, id_socio, ejemplar.id_ejemplar)
    _PRESTAMOS.append(prestamo)

    # 5. Notificar al socio sobre el nuevo préstamo
    socios.registrar_prestamo_socio(id_socio, nuevo_id_p)

    return True, f"Préstamo realizado con éxito (ID: {nuevo_id_p}). Caduca el: {prestamo.fecha_caducidad.strftime('%Y-%m-%d')}"

def devolver_prestamo(id_prestamo):
    p = None
    for prestamo in _PRESTAMOS:
        if prestamo.id_prestamo == id_prestamo and not prestamo.devuelto:
            p = prestamo
            break

    if not p:
        return False, "No se encontró un préstamo activo con ese ID."

    p.devuelto = True
    catalogo.marcar_disponible(p.id_ejemplar)
    socios.registrar_devolucion_socio(p.id_socio, p.id_prestamo)
    return True, "Libro devuelto correctamente."