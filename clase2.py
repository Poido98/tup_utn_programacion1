#ACA LO USE PARA PRACTICAR ALGUNAS FUNCIONES O MODIFICARLAS


# 10 - Crear una funcion con parametros, que dada una palabra, cuente la cantidad total de letras y retorne dicha cantidad como un numero entero
def contar_letras_texto(texto: str) -> int:
    """La funcion cuenta la cantidad total de letras que tiene una palabra

    Args:
        palabra (str): Indica cual es la palabra

    Returns:
        La cantidad total de letras que tiene 
    """
    contador_caracteres = 0

    #PUEDE SER CARACTER O _ (GUION BAJO)
    for caracter in texto:
        contador_caracteres += 1

    return contador_caracteres


# 11 - Crear una funcion sin parametros que pida al usuario que ingrese tres palabras, luego calculará cual de ellas tiene mayor cantidad de letras y tendra que imprimirla en consola junto con la cantidad de letras que posee
def ingresar_palabras():

    cantidad_mayor_caracteres = None
    palabra_mas_larga = None

    for i in range(3):

        palabra = input(f"Ingrese la {i + 1}° palabra: ")

        if cantidad_mayor_caracteres == None or contar_letras_texto(palabra) > cantidad_mayor_caracteres:
            
            cantidad_mayor_caracteres = contar_letras_texto(palabra)
            palabra_mas_larga = palabra

    texto = f"La palabra con mas cantidad de letras es: {palabra_mas_larga} y tiene un total de {cantidad_mayor_caracteres} caracteres."


    print(texto)

ingresar_palabras()
