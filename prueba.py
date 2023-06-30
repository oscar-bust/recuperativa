lista_marca = []
lista_patente  = []
lista_precio = []
lista_dueños = []
lista_rut = []

def menu():
    print('menu')
    print('[1] ingresar vehiculo ')
    print('[2] buscar patente ')
    print('[3] ver patentes inscritas')
    print('[4] buscador de marca' )
    print('[5] ver marcas inscritas ')
    print('[6] ver dueños inscritos ')
    print('[7]  salir')
# intente hacer un buscador pero aparentemente falle
def buscador_patente(cadena, letra):
    lista_patente(input('ingrese patente'))
    lista_patente= []
    for i in range(len(cadena)):
        if cadena[i] == letra:
            lista_patente
        return lista_patente

def buscador_marca(cadena, letra):
    
    lista_marca= []
    for i in range(len(cadena)):
        if cadena[i] == letra:
            lista_marca
        return lista_marca



while True:
    menu()
    opc = input('ingrese opcion ')

    if opc == '1':
        patente = input('ingresar patente ')
        dueño  = input('ingrese su nombre ')
        Rut = input('ingrese su rut ')
        marca = input('ingrese marca de su auto ')
        precio = input('ingrese el valor de su vehiculo ')
        lista_dueños.append(dueño)
        lista_patente.append(patente)
        lista_marca.append(marca)
        lista_precio.append(precio)      
    elif opc == '2':
       buscador_patente()
        
    elif opc == '3':
        print(lista_patente)
    elif opc == '4':
        buscador_marca()    
    elif opc == '5':
        print(lista_marca)
    elif opc == '6':
        print(lista_dueños)
    elif opc == '7':
        break



    
        

