"""#Funcion para calcular area del tringulo
def calcular_area(base,altura):
 print("#Formula para calcular el area de un Triangulo (-_-)")
 base = input('Ingresa tu base: ')
 altura = input('Ingresa tu altura: ')
 calculo = int(base) * int(altura) / 2
 if calculo >= 1000:
     calculo = int(base) * int(altura) // 2
 print (f"El area de tu triangulo es: {calculo} m")

calcular_area(0,0)
"""
#Codigo Refactorizado por chatGPT...
"""
    Calcula el área de un triángulo.

    Args:
    base (float): La base del triángulo.
    altura (float): La altura del triángulo.

    Returns:
    float: El área calculada del triángulo.
    """
def calcular_area(base=None, altura=None):
    if base is None:
        base = float(input('Ingresa la base del triángulo: '))
    if altura is None:
        altura = float(input('Ingresa la altura del triángulo: '))

    area = base * altura / 2
    print(f"El área del triángulo es: {area} m²")
    
calcular_area()
