"""
================================
 Tarea 4 - Suite de Tests (unittest)
 Autor: Diego Pacheco
================================

Pruebas unitarias para las funciones de la Tarea 2 (esBinario) 
y Tarea 3 (estaEnRango, estaEnLista), asegurando la cobertura 
de casos límite y comportamientos no deseados.
"""

import unittest
from src.binario import esBinario
from src.lista import estaEnRango, estaEnLista
#Diego Pacheco
class TestEsBinario(unittest.TestCase):

    def test_valores_validos(self):
        self.assertTrue(esBinario("0"))
        self.assertTrue(esBinario("1"))
        self.assertTrue(esBinario("10101"))

    def test_valores_invalidos(self):
        self.assertFalse(esBinario("102"))
        self.assertFalse(esBinario("hola"))
        self.assertFalse(esBinario("10A01"))

    def test_cadena_vacia(self):
        self.assertFalse(esBinario(""))

    def test_tipo_incorrecto(self):
        self.assertFalse(esBinario(None))
        self.assertFalse(esBinario(1010))


class TestEstaEnRango(unittest.TestCase):

    def test_en_rango(self):
        self.assertTrue(estaEnRango(5, 1, 10))
        self.assertTrue(estaEnRango(1, 1, 10))  # límite inferior
        self.assertTrue(estaEnRango(10, 1, 10)) # límite superior

    def test_fuera_de_rango(self):
        self.assertFalse(estaEnRango(0, 1, 10))
        self.assertFalse(estaEnRango(11, 1, 10))

    def test_tipos_incorrectos(self):
        self.assertFalse(estaEnRango("5", 1, 10))
        self.assertFalse(estaEnRango(5, "1", 10))
        self.assertFalse(estaEnRango(5, 1, "10"))
        self.assertFalse(estaEnRango(None, 1, 10))


class TestEstaEnLista(unittest.TestCase):

    def test_en_lista(self):
        self.assertTrue(estaEnLista(2, [1, 2, 3]))

    def test_no_en_lista(self):
        self.assertFalse(estaEnLista(10, [1, 2, 3]))

    def test_lista_vacia(self):
        self.assertFalse(estaEnLista(1, []))

    def test_valor_none(self):
        self.assertTrue(estaEnLista(None, [None, 1, 2]))
        self.assertFalse(estaEnLista(None, [1, 2, 3]))

    def test_lista_none(self):
        with self.assertRaises(TypeError):
            estaEnLista(1, None)


if __name__ == "__main__":
    unittest.main()
