class Usuario(object):
    def __init__(self,id,nombre,apellido,email,usuario,password) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.usuario = usuario
        self.password = password
        self.estado = True
        

    def cambiar_estado(self):
        '''Cambia el estado del usuario'''
        if self.estado:
            self.estado = False
        else:
            self.estado = True
        
    def __str__(self) -> str:
        return f"Usuario: {self.id} - {self.nombre} - {self.apellido} - {self.email} - {self.usuario} - {self.estado}"
       