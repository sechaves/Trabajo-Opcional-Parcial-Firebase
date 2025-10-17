import uuid
from dataclasses import dataclass, asdict

@dataclass
class Libro:
    titulo: str
    autor: str
    categoria: str
    isbn: int

    # Atributos para el sistema
    id: str = ""  # ID único para la base de datos
    disponible: bool = True

    def __post_init__(self):
        # Genera un ID único si no se proporciona uno
        if not self.id:
            self.id = str(uuid.uuid4())

    def to_dict(self):
        # Convierte el objeto en un diccionario para Firebase
        return asdict(self)

    def obtener_isbn(self):
        return self.isbn

    def obtener_info_libro(self):
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Categoria: {self.categoria} | ISBN: {self.isbn}"