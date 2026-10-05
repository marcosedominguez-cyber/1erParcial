"""Escriba aquí sus pruebas. No borre ni modifique tests/test_base.py.

Cada función de prueba comienza con test_ y usa assert.
Agregue al menos los cuatro casos descritos en el README.
Los imports ya están preparados; deepcopy crea una copia independiente
de la lista y de los diccionarios para comprobar que no se modificaron.
"""
from copy import deepcopy

from reservas import modificar_reserva


# Ejemplo de estructura, sin solución del caso:
# def test_nombre_del_comportamiento():
#     datos = [...]
#     antes = deepcopy(datos)
#     resultado = modificar_reserva(datos, ...)
#     assert resultado == "..."
#     assert datos == antes  # Cuando la operación debe conservar TODO.

def test_confirmar_no_existe():
    datos = [dict(id="R1", sala="A", inicio=540, fin=600,
                  estado="confirmada")]
    assert modificar_reserva(datos, "R2", 720, 780) == "NO_EXISTE"

def test_confirmar_cancelada():
    datos = [dict(id="R1", sala="A", inicio=540, fin=600,
                  estado="cancelada")]
    assert modificar_reserva(datos, "R1", 720, 780) == "CANCELADA"

def test_confirmar_cambio_de_horario_invalido():
    datos = [dict(id="R1", sala="A", inicio=540, fin=600,
                  estado="confirmada")]
    assert modificar_reserva(datos, "R1", -1, 1500) == "HORARIO_INVALIDO"

def test_confirmar_modificacion_valida():
    datos = ([dict(id="R1", sala="A", inicio=540, fin=600,estado="confirmada")])
    antes= deepcopy(datos)
    assert modificar_reserva(datos, "R1", 720, 780) == "OK"
    assert len(antes) == len(datos)
    assert antes[0]["estado"] == datos[0]["estado"]

def test_conflicto_de_horario():
    datos = [dict(id="R1", sala="A", inicio=540, fin=600,
                  estado="confirmada")]
    antes= deepcopy(datos)
    assert modificar_reserva(datos, "R1", 570, 630) == "CONFLICTO"
    assert datos == antes