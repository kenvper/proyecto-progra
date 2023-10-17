class Empresa():
    def __init__(self, id, nombre, direccion, telefono, email, contacto):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.contacto = contacto

    def __str__(self):
        return "Empresa: {0} - {1} - {2} - {3} - {4} - {5}".format(self.id, self.nombre, self.direccion, self.telefono, self.email, self.contacto)