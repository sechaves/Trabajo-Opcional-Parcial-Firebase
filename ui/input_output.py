from domain.libro import Libro
from domain.usuario import Usuario

def obtener_opcion():
    """Pide al usuario que elija una opción del menú."""
    return input("Selecciona una opción : ")

def obtener_datos_libro():
    """Pide al usuario todos los datos para crear un libro nuevo."""
    print("\n--- Agregar Nuevo Libro ---")
    titulo = input("Título del libro: ")
    autor = input("Autor del libro: ")
    categoria = input("Categoría: ")
    isbn = input("ISBN (solo números): ")
    return titulo, autor, categoria, isbn

def obtener_datos_usuario():
    """Pide al usuario los datos para registrar un nuevo usuario."""
    print("\n--- Registrar Nuevo Usuario ---")
    nombre = input("Nombre completo del usuario: ")
    documento = input("Documento de identidad (solo números): ")
    programa = input("Programa o carrera: ")
    return nombre, documento, programa

def mostrar_lista_libros(libros: list[Libro]):
    """Muestra una lista formateada de todos los libros."""
    print("\n--- Catálogo de Libros ---")
    
    # Maneja el caso de que ocurra un error al cargar los libros
    if libros is None:
        print("Hubo un error al cargar los libros desde la base de datos.")
        return
        
    # Maneja el caso de que no haya libros registrados
    if not libros:
        print("No hay libros registrados en la biblioteca todavía.")
        return
    
    for libro in libros:
        print(f"{libro.obtener_info_libro()}")

def mostrar_mensaje(mensaje: str):
    """Muestra un mensaje genérico al usuario (de éxito, error, etc.)."""
    print(f"\n{mensaje}")
    
def mostrar_lista_usuarios(usuarios: list[Usuario]):
    """Muestra una lista formateada de todos los usuarios."""
    print("\n--- Listado de Usuarios ---")
    if usuarios is None:
        print("Hubo un error al cargar los usuarios desde la base de datos.")
        return
    if not usuarios:
        print("No hay usuarios registrados en la biblioteca todavía.")
        return
    
    for usuario in usuarios:
        print(f"{usuario.obtener_info()}")
        
def obtener_documento_usuario():
    print("\n---  Eliminar Usuario ---")
    return input("Introduce el documento del usuario que deseas eliminar: ")

def obtener_isbn_libro():
    print("\n--- Eliminar Libro ---")
    return input("Introduce el codigo ISBN del libro que deseas eliminar: ")