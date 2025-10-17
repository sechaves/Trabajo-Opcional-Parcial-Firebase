import uuid
from dataclasses import dataclass, asdict

@dataclass
class Usuario:
    nombre: str
    documento: int
    programa: str

    # Atributo para el sistema
    id: str = "" # ID único para la base de datos

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())

    def to_dict(self):
        return asdict(self)

    def obtener_documento(self):
        return self.documento

    def obtener_info(self):
        return f"Usuario: {self.nombre} | Documento: {self.documento} | Programa: {self.programa}"