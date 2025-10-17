from data.firebase import FirebaseRealtime
from domain.libro import Libro
from domain.usuario import Usuario

class BibliotecaViewModel:
    def __init__(self):
        self.servicio_libros = FirebaseRealtime(base_path="libros")
        self.servicio_usuarios = FirebaseRealtime(base_path="usuarios")

    def agregar_libro(self, titulo: str, autor: str, categoria: str, isbn: str) -> str:
        """
        Valida los datos de un libro, comprueba si el ISBN ya existe, 
        y si no, lo registra en la base de datos.
        """
        if not all([titulo, autor, categoria, isbn]):
            return "Error: Todos los campos del libro son obligatorios."
        try:
            isbn_int = int(isbn)
            libros_existentes = self.servicio_libros.list_all()
            if libros_existentes:
                for datos_libro in libros_existentes.values():
                    if datos_libro.get('isbn') == isbn_int:                        
                        return f"Error: Ya existe un libro registrado con el ISBN '{isbn_int}'."
        except ValueError:
            return "Error: El ISBN debe ser un número válido."
        except Exception as e:
            return f"Error inesperado al guardar el libro: {e}"

    def listar_libros(self):
        try:
            libros_dict = self.servicio_libros.list_all()
            if not libros_dict:
                return []
            lista_de_libros = [Libro(**datos) for datos in libros_dict.values()]
            return lista_de_libros
        except Exception as e:
            print(f"Error al obtener los libros: {e}")
            return None

    def registrar_usuario(self, nombre: str, documento: str, programa: str):
        if not all([nombre, documento, programa]):
            return "Error: Todos los campos del usuario son obligatorios."
            
        try:
            doc_int = int(documento)
            if self.servicio_usuarios.read(str(doc_int)):
                return f"El usuario con documento '{doc_int}' ya está registrado."
            
            nuevo_usuario = Usuario(nombre=nombre, documento=doc_int, programa=programa)
            self.servicio_usuarios.create(str(doc_int), nuevo_usuario.to_dict())
            return f"Usuario '{nombre}' registrado con éxito."
        except ValueError:
            return "Error: El documento debe ser un número válido."
        except Exception as e:
            return f"Error inesperado al registrar el usuario: {e}"
        
    def listar_usuarios(self):
        try:
            usuarios_dict = self.servicio_usuarios.list_all()
            if not usuarios_dict:
                return[]
            lista_de_usuarios = [Usuario(**datos) for datos in usuarios_dict.values()]
            return lista_de_usuarios
        except Exception as e:
            print(f"Error al obtener los usuarios: {e}")
            return None
        
    def eliminar_libro(self, isbn_a_eliminar: str):
        try:
            isbn_num = int(isbn_a_eliminar)
            libros_dict = self.servicio_libros.list_all()
            
            id_del_libro_para_borrar = None
            # Buscamos en todos los libros cuál coincide con el ISBN
            for id_libro, datos_libro in libros_dict.items():
                if datos_libro.get('isbn') == isbn_num:
                    id_del_libro_para_borrar = id_libro
                    break
            
            if id_del_libro_para_borrar:
                self.servicio_libros.delete(id_del_libro_para_borrar)
                return f"Libro con ISBN '{isbn_num}' eliminado correctamente."
            else:
                return f"No se encontró ningún libro con el ISBN '{isbn_num}'."
        except ValueError:
            return "Error: El ISBN debe ser un número."
        except Exception as e:
            return f"Error inesperado al eliminar el libro: {e}"

    def eliminar_usuario(self, documento_a_eliminar: str) -> str:
        try:
            if self.servicio_usuarios.read(documento_a_eliminar):
                self.servicio_usuarios.delete(documento_a_eliminar)
                return f"Usuario con documento '{documento_a_eliminar}' eliminado correctamente."
            else:
                return f"No se encontró ningún usuario con el documento '{documento_a_eliminar}'."
        except Exception as e:
            return f"Error inesperado al eliminar el usuario: {e}"