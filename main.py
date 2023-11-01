from controller import UsuarioController

if __name__ == "__main__":
    CRUD = UsuarioController()
    
    
    CRUD.cargar_usuarios_desde_txt('ejemplo.txt')
    
    CRUD.inactivar_usuario('jjvvquez')
    
    lista =  CRUD.usuarios
    
    if len(lista) != 0:
        for elemento in lista:
            print(elemento)   
    else:    
        print('No hay datos en memoria , Sistema CAIDO')
    

    
    
    
    

        
        
        


