"""
================================
 Tarea 5 - Suite de Tests (pytest)
 Autor: Diego Pacheco
================================

Pruebas unitarias para las funciones de la Tarea 2 y Tarea 3 
utilizando el framework pytest para una sintaxis más simple y directa.
"""
from src.binario import esBinario
from src.lista import estaEnRango, estaEnLista
import pytest

# ---------- esBinario ----------

def test_esBinario_valido():
    assert esBinario("1010")
    assert esBinario("0")
    assert esBinario("1")

def test_esBinario_invalido():
    assert not esBinario("hola")
    assert not esBinario("102")
    assert not esBinario("10A01")
    assert not esBinario("")

def test_esBinario_tipo_incorrecto():
    assert not esBinario(None)
    assert not esBinario(1010)

# ---------- estaEnRango ---------- Diego Pacheco

def test_estaEnRango_correcto():
    assert estaEnRango(5, 1, 10)
    assert estaEnRango(1, 1, 10)
    assert estaEnRango(10, 1, 10)

def test_estaEnRango_fuera():
    assert not estaEnRango(0, 1, 10)
    assert not estaEnRango(11, 1, 10)

def test_estaEnRango_tipos_incorrectos():
    assert not estaEnRango("5", 1, 10)
    assert not estaEnRango(5, "1", 10)
    assert not estaEnRango(5, 1, "10")
    assert not estaEnRango(None, 1, 10)

# ---------- estaEnLista ----------

def test_estaEnLista_normal():
    assert estaEnLista(2, [1, 2, 3])
    assert not estaEnLista(5, [1, 2, 3])

def test_estaEnLista_vacia():
    assert not estaEnLista(3, [])

def test_estaEnLista_none():
    assert estaEnLista(None, [None, 1, 2])
    assert not estaEnLista(None, [1, 2])

def test_estaEnLista_lista_none():
    with pytest.raises(TypeError):
        estaEnLista(1, None)
