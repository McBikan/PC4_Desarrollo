import pytest
from servicios.servicios_usuarios import ServicioUsuarios

@pytest.fixture
def servicio_usuarios():
    return ServicioUsuarios()

def test_crear_usuario(servicio_usuarios):
    usuario = servicio_usuarios.crear_usuario("Cesar Lara", "cesarlara@uni.pe")
    assert usuario["nombre"] == "Cesar Lara"
    assert usuario["correo"] == "cesarlara@uni.pe"

def test_obtener_usuario_por_id(servicio_usuarios):
    usuario = servicio_usuarios.crear_usuario("Brian Huaman", "bhuamang@uni.pe")
    usuario_obtenido = servicio_usuarios.obtener_usuario(usuario["id"])
    assert usuario_obtenido["nombre"] == "Brian Huaman"
