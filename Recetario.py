from pathlib import Path

def obtener_directorio():
    base = Path.home()
    ruta = Path(base, "Recetas")
    return ruta

def ejecutar_menu():
    opcion = 0
    while (opcion != 6):
        mostrar_menu()
        opcion = opcion_menu()
        if(opcion in range(1,7)):
            ejecutar_opcion(opcion)

def mostrar_menu():
    print(("|--------MENU--------|\n"
          "[1] - Leer receta \n"
          "[2] - Crear receta \n"
          "[3] - Crear categoría \n"
          "[4] - Eliminar receta \n"
          "[5] - Eliminar receta \n"
          "[6] - Finalizar programa \n"))

def opcion_menu():
    opcion = input("Ingresa una opción: ")
    if opcion.isnumeric() == True:
        opcion = int(opcion)
        return opcion
    else:
        print("Ingresa un número...")

def ejecutar_opcion(opcion):
    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            print("Hasta luego!")
        case _:
            ejecutar_menu()


#################   MAIN    ##################
print(f"Bienvenido! Este es un programa para un recetario! :)\n"
      f"Tus recetas se encuentran en: {obtener_directorio()}")
ejecutar_menu()
