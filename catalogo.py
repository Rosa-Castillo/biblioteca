class Catalogo:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor):
        libro = {"titulo": titulo, "autor": autor}
        self.libros.append(libro)
        print(f"Libro '{titulo}' añadido correctamente.")

    def mostrar_catalogo(self):
        if not self.libros:
            print("El catálogo está vacío.")
        else:
            print("\n--- CATÁLOGO DE LIBROS ---")
            for i, libro in enumerate(self.libros, 1):
                print(f"{i}. {libro['titulo']} - {libro['autor']}")