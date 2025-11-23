"""
================================
 Tarea 2 - Conversión Binario
 Autor: Diego Pacheco
================================

Verifica si la entrada es un binario y lo convierte a decimal.
"""
def esBinario(strbinario):
    if not isinstance(strbinario, str):
        return False
    if strbinario == "":
        return False
    return all(c in "01" for c in strbinario)

if __name__ == "__main__":
    print("\n[ Conversión Binario → Decimal ]")

    numero = input("Introduce un número binario: ")

    if esBinario(numero):
        decimal = int(numero, 2)
        print(f"El número decimal es: {decimal}")
    else:
        print("La cadena introducida NO es un número binario válido.")
