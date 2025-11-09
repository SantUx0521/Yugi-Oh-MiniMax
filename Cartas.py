class cartas:
    def __init__(self, id, nombre, ataque, defensa, tipo):
        self.id = id
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.tipo = tipo
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Ataque: {self.ataque}, Defensa: {self.defensa}, Tipo: {self.tipo}"
        