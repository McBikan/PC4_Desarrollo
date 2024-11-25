import pytest
from repositorios.repositorio_productos import RepositorioProductos

@pytest.fixture
def repositorio():
    return RepositorioProductos()

def test_crear_producto(repositorio):
    producto = repositorio.crear_producto("Laptop", 1500, 1)
    assert producto["id"] == 1
    assert producto["nombre"] == "Laptop"
    assert producto["precio"] == 1500
    assert producto["usuario_id"] == 1

def test_obtener_producto_por_id(repositorio):
    repositorio.crear_producto("Laptop", 1500, 1)
    producto = repositorio.obtener_producto_por_id(1)
    assert producto["nombre"] == "Laptop"
    assert producto["precio"] == 1500

def test_actualizar_producto(repositorio):
    repositorio.crear_producto("Laptop", 1500, 1)
    producto_actualizado = repositorio.actualizar_producto(1, nombre="Laptop Profesional", precio=2000)
    assert producto_actualizado["nombre"] == "Laptop Profesional"
    assert producto_actualizado["precio"] == 2000

def test_eliminar_producto(repositorio):
    repositorio.crear_producto("Laptop", 1500, 1)
    producto_eliminado = repositorio.eliminar_producto(1)
    assert producto_eliminado["nombre"] == "Laptop"
    assert repositorio.obtener_producto_por_id(1) is None
