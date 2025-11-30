"""
================================
 Tarea 3 - Utilidades de Lista
 Autor: Diego Pacheco
================================
"""

def estaEnRango(valor, minimo, maximo):
    """Devuelve True si valor está entre minimo y maximo (inclusive)."""
    # Validación de tipos para asegurar reutilización segura
    if not (isinstance(valor, (int, float)) and 
            isinstance(minimo, (int, float)) and 
            isinstance(maximo, (int, float))):
        return False
    
    return minimo <= valor <= maximo

def estaEnLista(valor, lista):
    """Devuelve True si valor está dentro de la lista."""
    return valor in lista

if __name__ == "__main__":
    # 1. Solicitamos el número
    try:
        numero = int(input("Introduce un número del 1 al 20: "))
    except ValueError:
        print("Error: Por favor introduce un número entero válido.")
        exit()

    # 2. Ajustamos las variables según el enunciado
    minimo = 1
    maximo = 20  # El enunciado pide hasta 20
    lista = [6, 14, 11, 3, 2, 1, 15, 19] # La lista específica del ejercicio

    # 3. Implementamos la lógica
    if estaEnRango(numero, minimo, maximo):
        print(f"Correcto: El número {numero} está dentro del rango ({minimo}-{maximo}).")
        
        # Solo si está en rango, comprobamos si está en la lista
        if estaEnLista(numero, lista):
            print(f"¡Éxito! El número {numero} ESTÁ en la lista secreta.")
        else:
            print(f"El número {numero} NO está en la lista.")
            
    else:
        print(f"Error: El número debe estar entre {minimo} y {maximo}.")
