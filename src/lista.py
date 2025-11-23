"""
================================
 Tarea 3 - Utilidades de Lista
 Autor: Diego Pacheco
================================

Implementa las funciones estaEnRango y estaEnLista para verificar 
valores dentro de un rango y en una lista, respectivamente.
"""
def estaEnRango(valor, minimo, maximo):
    if not (isinstance(valor, (int, float)) and
            isinstance(minimo, (int, float)) and
            isinstance(maximo, (int, float))):
        return False
    
    return minimo <= valor <= maximo


def estaEnLista(valor, lista):
   
    #Devuelve True si valor está dentro de la lista.
   
    return valor in lista


if __name__ == "__main__":
    numero = int(input("Introduce un número: "))

    minimo = 1
    maximo = 10
    lista = [2, 4, 6, 8, 10]

    print("¿Está en rango?:", estaEnRango(numero, minimo, maximo))
    print("¿Está en la lista?:", estaEnLista(numero, lista))
