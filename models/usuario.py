class Usuario(object):
    def __init__(self,nombre,apellido,usuario,password,estado=True) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.estado = estado
        

    def cambiar_estado(self):
        '''Cambia el estado del usuario'''
        if self.estado:
            self.estado = False
        else:
            self.estado = True
        
    def __str__(self) -> str:
        return f"Usuario:  {self.nombre} - {self.apellido} - {self.usuario} - {self.estado}"
       