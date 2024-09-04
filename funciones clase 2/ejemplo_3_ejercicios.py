# 1 - Crear una funcion sin parámetros que imprima 'Bienvenidos a la UTN'
def bienvenida() -> None:
    """
    La funcion imprime con el mensaje 'Bienvenidos a la UTN'
    """
    print('Bienvenidos a la UTN')

# 2 - Crear una funcion sin parametros que retorne el año actual como numero entero
def año_actual() -> int:
    """
    La funcion retorna el año actual
    """
    año = int(2024)
    return año

print(año_actual())

# 3 - Crear una funcion que dado un parametro que corresponde a un nombre, salude
def saludar(nombre: str) -> None:
    """
    La funcion saluda al nombre indicado

    Args:
        nombre (str): nombre del usuario

    """
    print(f"Hola {nombre}")

saludar("Nahuel")

# 4 - Crear una función que dado una base y una altura, calcule y retorne el area de un rectángulo
def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula el area de un rectangulo indicando su base y altura

    Args:
        base (float): Indica la base del rectangulo a calcular
        altura (float): Indica la altura del rectangulo a calcular

    Returns:
        Retorna el area total de un rectangulo
    """
    area = (base * altura)
    print(f'El rectángulo de base {base} y altura {altura} tiene un area de {area}')
    return area

# 5 - Crear una funcion con parametros que dado un radio, calcule el area de un circulo
def calcular_area_circulo(radio: float, pi = 3.14) -> float:
    """Calcula el area de un circulo inicando su radio

    Args:
        radio (float): Se coloca el radio que tiene el circulo
        pi (3.14): Es el valor de pi, es una constante

    Returns:
        Retorna el area total del circulo
    """
    area = pi * (radio ** 2)
    print(f"El circulo de radio {radio} tiene un area de {area}")
    return area

calcular_area_circulo(5)


# 6 - Crear una funcion con parámetros que dado dos numeros, retorne True si son multiplos, false caso contrario
def es_multiplo(numero_a: int, numero_b: int) -> bool:
    """La funcion analiza si esos dos numeros ingresados son multiplos o no

    Args:
        numero_a (int): Primer numero dado
        numero_b (int): Segundo numero dado

    Returns:
        Retorna true si son multiplos o false si no lo son
    """
    check_multiplo = numero_a % numero_b == 0
    return check_multiplo


# 7 - Crear una funcion con parámetros que dado un numero, retorne si el numero es primo o no.
def validar_si_es_primo(numero_a_verificar_primalidad: int) -> bool:
    """La funcion analiza si el numero ingresado es primo o no

    Args:
        numero_a_verificar_primalidad (int): Es el numero a verificar

    Returns:
        Si es primo o no es primo
    """
    # Arrancamos con que es divisible por si mismo y por 1, con lo cual decimos que tiene al menos dos divisores
    if numero_a_verificar_primalidad < 2:
        return False
    
    contador_divisores = 2
    posible_divisor = 2

    while posible_divisor < numero_a_verificar_primalidad:
        if es_multiplo(numero_a_verificar_primalidad, posible_divisor):
            contador_divisores += 1
            # si encontramos un tercer divisor lo sumamos al contador
            # y cortamos el bucle
            break
        posible_divisor += 1
    # Si tiene mas de 2 divisores, no es un numero primo
    es_primo = contador_divisores == 2
    return es_primo


# 8 - Crear una funcion con parámetros que dado un numero, recorra todos los numeros anteriores y diga cual de ellos es numero primo y cuales no lo es.
def mostrar_numeros_primos_hasta(numero_tope_a_verificar_primalidad: int) -> None:
    """La funcion, a partir de un numero ingresado, recorre todos los anteriores y determina cual es primo y cual no

    Args:
        numero_tope_a_verificar_primalidad (int): Es el numero a ingresar 
    """
    for numero in range(0, numero_tope_a_verificar_primalidad + 1):
        if validar_si_es_primo(numero):
            texto = f'El número {numero} ES PRIMO'
        else:
            texto = f'El número {numero} NO ES PRIMO'
        print(texto)

# 9 - Crear una funcion con parametros que dada una palabra y una letra, retorne la cantidad de letras coincidentes que tiene esa palabra
def mostrar_letras_coincidentes_en_palabra(palabra: str, letra: str) -> int:
    """Dada una palabra y una letra retorna la cantidad de veces que esa letra aparece en la palabra

    Args:
        palabra (str): Se le da una palabra
        letra (str): Se le da una letra

    Returns:
        Retorna la cantidad de veces que se repite esa letra en la palabra
    """
    contador_letras = 0
    # NO SE COMO SE USA CHAR Y DUDAS EN LINEAS 135 136 Y 137
    for char in palabra:
        if char == letra:
            contador_letras += 1
    
    print(f"En la palabra {palabra} la letra {letra} se repite {contador_letras} veces.")
    return contador_letras

mostrar_letras_coincidentes_en_palabra("programacion", "o")


# 10 - Crear una funcion con parametros, que dada una palabra, cuente la cantidad total de letras y retorne dicha cantidad como un numero entero
def contar_letras_texto(texto: str) -> int:
    """La funcion cuenta la cantidad total de letras que tiene una palabra

    Args:
        texto (str): Indica cual es la palabra

    Returns:
        La cantidad total de letras que tiene 
    """
    contador_caracteres = 0

    #PUEDE SER CARACTER O _ (GUION BAJO) CORREGIR 
    for caracter in texto:
        contador_caracteres += 1

    return contador_caracteres

contar_letras_texto("computadora")


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


bienvenida()

calcular_area_rectangulo(15, 4)
calcular_area_rectangulo(altura=4, base=15)

print(es_multiplo(15,4))

mostrar_numeros_primos_hasta(20)

print(año_actual())

calcular_area_circulo(5)
