import funciones

def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t...:::: AGREGAR CARACTERÍSTICAS DE UNA PELICULA::::...\n")
    caracteristica=input("Introducir el nombre de la característica: ").lower().strip()
    valor=input(f"Introducir el valor de {caracteristica}: ").lower().strip()
    pelis[caracteristica] = valor
    funciones.accionExitosa()

def mostrarPeliculas(pelis):
    print("\n\t\t...:::: MOSTRAR CARACTERISTICA ::::...\n")
    if (len(pelis) > 0):
        for i in pelis:
            print(f"{i}\t\t{pelis[i]}")
        funciones.espereTecla()
    else:
        input("No se encontró el valor ingresado. [ENTER]:")
    
def limpiarPeliculas(pelis):
    opc = ""
    if len(pelis)>0:
        while opc!="si" and opc!="no":
            opc=input("¿Deseas borrar todas las caracteristicas? ").lower().strip()
        if (opc == "si"):
            pelis=pelis.clear()
            funciones.accionExitosa()
    else:
        input("...¡No hay peliculas que limpiar!...") 
        
def buscarPeliculas(pelis):
    print("\n\t\t...:::: BUSCAR UNA CARACTERÍSTICA DE UNA PELICULA ::::...\n")
    caracteristica=input("Escribir el nombre de la característica: ").upper().strip()
    noencontrado = True

    for i in pelis:
        if caracteristica==i:
            print("\tCaracteristica\t\tValor\n")
            print(f"{i}\t\t{pelis[i]}")
            noencontrado = False
        funciones.espereTecla()
    if noencontrado:
        input("...¡No exite la característica que estas buscando, verifique!...")

def borrarPeliculas(pelis):
    print("\n\t\t...:::: BORRAR LA CARACTERÍSTICA DE LA PELICULA ::::...\n")
    caracteristica=input("Escribir el nombre de la característica: ").upper().strip()
    encontrado = True
    for i in pelis:
        if i == caracteristica:
            print("\tCaracterística:\t\tValor")
            print(f"\t{i}\t\t{pelis[i]}")
            opc = ""
            encontrado = False
    if encontrado:
        while opc!="si" and opc!="no":
            opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
        if (opc == "si"):
            pelis.pop(caracteristica)
            funciones.accionExitosa()
    else:
        input("...¡No exite la característica que estas buscando, verifique!...")
        
def modificarPeliculas(pelis):
    print("\n\t\t...:::: MODIFICAR LA CARACTERÍSTICA DE LA PELICULA ::::...\n")
    caracteristica=input("Escribir el nombre de la característica: ").upper().strip()
    noencontrado = True
    for i in pelis:
        if i == caracteristica:
            print("\tCaracterística:\t\tValor")
            print(f"\t{i}\t\t{pelis[i]}")
            opc = ""
            noencontrado = False
            nuevo_valor=input("Escribir el valor de la característica: ").upper().strip()
            while opc!="si" and opc!="no":
                opc=input("¿Deseas modificar la característica? (Si/No): ").lower().strip()
            if (opc == "si"):
                print(f"{pelis[caracteristica]} ---> {nuevo_valor}")
                pelis[caracteristica] = nuevo_valor
                funciones.accionExitosa()
            else:
                print("Acción cancelada...")
    if noencontrado:
        input("...¡No exite la característica que estas buscando, verifique!...")