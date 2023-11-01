from models import Usuario


class UsuarioController:
    def __init__(self):
        """
        Inicializa una nueva instancia del UsuarioController.

        Este constructor inicializa una lista vacía para almacenar objetos de Usuario.
        """
        self.usuarios:Usuario = []

    def agregar_usuario(self, nombre, apellidos, usuario, password):
        """
        Agrega un nuevo usuario a la lista de usuarios.

        Args:
            nombre (str): El nombre del usuario.
            apellidos (str): Los apellidos del usuario.
            usuario (str): El nombre de usuario del usuario.
            password (str): La contraseña del usuario.

        Este método verifica si el usuario ya existe y agrega un nuevo usuario a la lista
        si no se encuentra. También actualiza el estado del usuario a 'Activo' si se agrega.
        """
        if not self.consultar_usuario(usuario):
            nuevo_usuario = Usuario(nombre, apellidos, usuario, password)
            self.usuarios.append(nuevo_usuario)
            print(f'Usuario {usuario} registrado exitosamente.')
        else:
            print(f'El usuario {usuario} ya existe en el sistema.')

    def consultar_usuario(self, usuario):
        """
        Busca un usuario en la lista por su nombre de usuario.

        Args:
            usuario (str): El nombre de usuario a buscar.

        Returns:
            Usuario: El objeto de usuario si se encuentra, None si no se encuentra.

        Este método busca un usuario en la lista por su nombre de usuario y devuelve el objeto
        de usuario si se encuentra. Si el usuario no se encuentra, devuelve None.
        """
        for user in self.usuarios:
            if user.usuario == usuario:
                return user
        return None

    def inactivar_usuario(self, usuario):
        """
        Establece el estado de un usuario en 'Inactivo'.

        Args:
            usuario (str): El nombre de usuario del usuario que se va a inactivar.

        Este método verifica si el usuario existe y establece su estado en 'Inactivo' si se encuentra.
        """
        user = self.consultar_usuario(usuario)
        if user:
            user.estado = 'Inactivo'
            print(f'Usuario {usuario} inactivado correctamente.')
        else:
            print(f'El usuario {usuario} no existe en el sistema.')

    def cargar_usuarios_desde_txt(archivo_txt):
        """
        Carga los datos de usuario desde un archivo de texto.

        Args:
            archivo_txt (str): La ruta al archivo de texto desde el cual cargar los datos.

        Returns:
            UsuarioController: Una nueva instancia de UsuarioController con los datos de usuario cargados.

        Este método lee los datos de usuario desde un archivo de texto, asumiendo un formato específico,
        y crea una nueva instancia de UsuarioController con los datos cargados. Devuelve la nueva instancia.
        """
        registro = UsuarioController()  # Crea una nueva instancia de RegistroUsuarios

        try:
            with open(archivo_txt, 'r') as file:
                for linea in file:
                    usuario, nombre, apellidos, password, estado = linea.strip().split(',')
                    registro.usuarios[usuario] = {
                        'nombre': nombre,
                        'apellidos': apellidos,
                        'password': password,
                        'estado': estado
                    }
            return registro
        except FileNotFoundError:
            print(f"El archivo {archivo_txt} no existe.")
            return None

    def guardar_usuarios_en_txt(self, archivo_txt):
        """
        Guarda los datos de usuario en un archivo de texto.

        Args:
            archivo_txt (str): La ruta al archivo de texto donde guardar los datos de usuario.

        Este método guarda los datos de usuario en un archivo de texto, siguiendo un formato específico.
        """
        with open(archivo_txt, 'w') as file:
            for usuario in self.usuarios:
                linea = f'{usuario.nombre},{usuario.apellido},{usuario.usuario},{usuario.password},{usuario.estado}\n'
                file.write(linea)

    def cargar_usuarios_desde_txt(self, archivo_txt):
        """
        Carga los datos de usuario desde un archivo de texto y actualiza la lista de usuarios.

        Args:
            archivo_txt (str): La ruta al archivo de texto desde el cual cargar los datos.

        Este método lee los datos de usuario desde un archivo de texto, asumiendo un formato específico,
        y actualiza la lista de usuarios con los datos cargados.
        """
        try:
            with open(archivo_txt, 'r') as file:
                self.usuarios = []
                for linea in file:
                    nombre, apellido, usuario, password, estado = linea.strip().split(',')
                    nuevo_usuario = Usuario(nombre, apellido, usuario, password)
                    self.usuarios.append(nuevo_usuario)
        except FileNotFoundError:
            print(f"El archivo {archivo_txt} no existe.")
