class Cliente(object):
    
    def __init__(self,nombre:str,apellido:str,dni:str,telefono:str)->None:
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        
    def __str__(self)->str:
        return f"El Nombre : {self.nombre} Apellido: {self.apellido} DNI: {self.dni} Telefono: {self.telefono}"