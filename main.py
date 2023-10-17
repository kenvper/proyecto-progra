from models import Cliente,Empresa,Usuario

if __name__ == "__main__":
    
    clientes:Cliente = []
    empresas:Empresa = []
    usuarios:Usuario = []
    
    nombre = "Kenneth"
    apellido = "Cedeno"
    dni = "117150965"
    telefono = "84662096"
    
    clientes.append(Cliente(nombre,apellido,dni,telefono))
    empresas.append(Empresa(1,"Intel","Heredia","22963125","HR@intel.com","Helen Rivera"))
    
    usuarios.append(Usuario(1,"Kenneth","Cedeno","ejemplo@gmail.com","ejemploLoco","Password123"))
    
    for cliente in clientes:
        print(cliente.__str__() + "\n")
    
    for empresa in empresas:
        print(empresa.__str__() + "\n")
        
    print("Usuarios antes de cambiar estados: \n")    
    for usuario in usuarios:
        print(usuario.__str__() + "\n")
    
    
    for usuario in usuarios:
        usuario.cambiar_estado()
        
    print("Usuarios despues de cambiar estados: \n")  
    for usuario in usuarios:
        print(usuario.__str__() + "\n")