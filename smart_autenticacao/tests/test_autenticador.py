import os
import pytest
from smart_autenticacao.autenticador import Autenticador

@pytest.fixture(autouse=True)
def configurar_variaveis(monkeypatch):
    # Define valores de ambiente simulados
    monkeypatch.setenv("LIBERAR_SMART_AUTENTICACAO", "true")
    monkeypatch.setenv("LIBERAR_MODULO_INEXISTENTE", "false")
    monkeypatch.setenv("LIBERAR_MODULO_FALSO", "false")

def test_modulo_liberado():
    aut = Autenticador()
    assert aut.verificar_modulo("SMART_AUTENTICACAO") is True

def test_modulo_nao_liberado_false():
    aut = Autenticador()
    assert aut.verificar_modulo("MODULO_FALSO") is False

def test_variavel_ausente(monkeypatch):
    monkeypatch.delenv("LIBERAR_MODULO_AUSENTE", raising=False)
    aut = Autenticador()
    assert aut.verificar_modulo("MODULO_AUSENTE") is False
