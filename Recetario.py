from pathlib import Path
import os
from os import system
def obtener_directorio():
    base = Path.home()
    ruta = Path(base, "Recetas")
    return ruta

def ejecutar_menu():
    opcion = 0
    directorio = obtener_directorio()
    print(f"\nBienvenido! Este es un programa para un recetario! :)\n"
          f"Tus recetas se encuentran en: {directorio}")

    while (opcion != 6):
        mostrar_menu()
        opcion = opcion_menu()
        if(opcion in range(1,7)):
            ejecutar_opcion(opcion,directorio)

def mostrar_menu():
    print(("\n|--------MENU--------|\n"
          "[1] - Leer receta \n"
          "[2] - Crear receta \n"
          "[3] - Crear categoría \n"
          "[4] - Eliminar receta \n"
          "[5] - Eliminar categoría \n"
          "[6] - Finalizar programa"))

def opcion_menu():
    opcion = input("Ingresa una opción: ")
    if opcion.isnumeric() == True:
        opcion = int(opcion)
        return opcion
    else:
        print("Ingresa un número...")

def mostrar_categorias(directorio): #Retorna una lista enumerada de las categorias
    listaCategorias = []
    print("\nLas categorías disponibles son: ")
    for item in Path(directorio).glob('*'):
        listaCategorias.append(os.path.split(item)[1])
    for i,j in enumerate(listaCategorias):
        print(f"[{i}] - {j}")
    return listaCategorias

def elegir_categorias(listaCategorias, directorio):
    opcCategoria = input("Ingresa el número de la categoría: ")
    if opcCategoria.isnumeric() == True:
        opcCategoria = int(opcCategoria)
        if opcCategoria < len(listaCategorias): #Dentro del rango de categorias?
            directorioCategoria = Path(directorio,listaCategorias[opcCategoria])
            return directorioCategoria
        else:
            print("Elige una categoría dentro del rango")
            elegir_categorias(listaCategorias, directorio)
    else:
        print("Ingresa el número de la categoría...")
        elegir_categorias(listaCategorias, directorio)

def mostrar_recetas(directorioCategoria):
    listaRecetas = []
    print("\nLas recetas disponibles son: ")
    for item in Path(directorioCategoria).glob('*'):
        listaRecetas.append(os.path.split(item)[1])
    for i,j in enumerate(listaRecetas):
        print(f"[{i}] - {j}")
    return listaRecetas

def elegir_recetas(listaRecetas,directorioCategoria):
    opcReceta = input("Ingresa el número de la receta: ")
    if opcReceta.isnumeric() == True:
        opcReceta = int(opcReceta)
        if opcReceta < len(listaRecetas): #Dentro del rango de categorias?
            directorioReceta = Path(directorioCategoria,listaRecetas[opcReceta])
            return directorioReceta
        else:
            print("Elige una receta dentro del rango")
            elegir_recetas(listaRecetas, directorioCategoria)
    else:
        print("Ingresa el número de la receta...")
        elegir_recetas(listaRecetas, directorioCategoria)

def leerArchivo_receta(directorioReceta):
    archivo = open(directorioReceta,'r')
    print(archivo.read())
    archivo.close()

def agregar_receta(directorioCategoria):
    nombreReceta = input("Ingresa el nombre de la receta, con la extension .txt: ")
    contenidoReceta = input(f"Ingresa el contenido de la receta '{nombreReceta}': ")
    nuevaReceta = open(Path(directorioCategoria,nombreReceta), 'w')
    nuevaReceta.write(contenidoReceta)
    nuevaReceta.close()
    print(f"Receta con el nombre '{nombreReceta}' agregada con éxito")

def agregar_categoria(directorio):
    nombreCategoria= input("Ingresa el nombre de la nueva categoría: ")
    nuevoDirectorio = os.makedirs(Path(directorio,nombreCategoria))

def eliminarArchivo_receta(directorioReceta):
    os.remove(directorioReceta)

def eliminar_categoria(directorioCategoria):
    os.rmdir(directorioCategoria)
def ejecutar_opcion(opcion,directorio):
    match opcion:
        case 1:
            listaCategorias = mostrar_categorias(directorio)
            if len(listaCategorias) != 0: #Comprobar que la lista no esté vacía
                directorioCategoria = elegir_categorias(listaCategorias, directorio)
                listaRecetas = mostrar_recetas(directorioCategoria)
                if len(listaRecetas) != 0:
                    directorioReceta = elegir_recetas(listaRecetas,directorioCategoria)
                    leerArchivo_receta(directorioReceta)
                    system('pause')
                    system('cls')
                else:
                    print("*Lista de recetas vacía*")
            else:
                print("*Lista de categorías vacía*")
        case 2:
            listaCategorias = mostrar_categorias(directorio)
            if len(listaCategorias) != 0:
                directorioCategoria = elegir_categorias(listaCategorias, directorio)
                listaRecetas = mostrar_recetas(directorioCategoria)
                agregar_receta(directorioCategoria)
                system('pause')
                system('cls')
            else:
                print("*Lista de categorías vacía*")
        case 3:
            listaCategorias = mostrar_categorias(directorio)
            agregar_categoria(directorio)
            system('pause')
            system('cls')
        case 4:
            listaCategorias = mostrar_categorias(directorio)
            if len(listaCategorias) != 0: #Comprobar que la lista no esté vacía
                directorioCategoria = elegir_categorias(listaCategorias, directorio)
                listaRecetas = mostrar_recetas(directorioCategoria)
                if len(listaRecetas) != 0:
                    directorioReceta = elegir_recetas(listaRecetas,directorioCategoria)
                    eliminarArchivo_receta(directorioReceta)
                    system('pause')
                    system('cls')
                else:
                    print("*Lista de recetas vacía*")
            else:
                print("*Lista de categorías vacía*")
        case 5:
            listaCategorias = mostrar_categorias(directorio)
            if len(listaCategorias) != 0: #Comprobar que la lista no esté vacía
                directorioCategoria = elegir_categorias(listaCategorias, directorio)
                eliminar_categoria(directorioCategoria)
                system('pause')
                system('cls')
            else:
                print("*Lista de categorías vacía*")
        case 6:
            print("Hasta luego!")
        case _:
            ejecutar_menu()


#################   MAIN    ##################
ejecutar_menu()
