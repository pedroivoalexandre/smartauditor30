# tests/test_env_loading.py

# Este arquivo de teste é responsável por verificar a funcionalidade da classe `EnvLoader`
# localizada em `smart_utils/env_loader.py`. Ele garante que o carregamento de variáveis
# de ambiente de um arquivo `.env` funciona corretamente.
# O foco principal deste teste é assegurar que a variável de ambiente `GEMINI_API_KEY`
# é carregada com sucesso, o que é crucial para a operação de outras partes do sistema
# que dependem dessa chave.

import pytest
from pathlib import Path
from smart_utils.env_loader import EnvLoader

class TestEnvLoading:
    """
    Classe de teste para a funcionalidade de carregamento de variáveis de ambiente.
    Verifica se a classe `EnvLoader` carrega e gerencia corretamente as variáveis
    de um arquivo `.env`, especificamente focando na `GEMINI_API_KEY`.
    """

    @pytest.fixture(autouse=True)
    def setup_method(self):
        """
        Fixture que é executada automaticamente antes de cada método de teste nesta classe.
        Ela configura o caminho para o arquivo `.env` principal do projeto
        (localizado em `smart_utils/.env`) e inicializa uma instância de `EnvLoader`
        para carregar as variáveis de ambiente desse arquivo.
        """
        self.caminho_env = Path(__file__).resolve().parent.parent / 'smart_utils' / '.env'
        self.loader = EnvLoader(self.caminho_env)

    def test_gemini_api_key_exists(self):
        """
        Testa se a variável de ambiente `GEMINI_API_KEY` é carregada com sucesso
        pelo `EnvLoader` e se o seu valor não é nulo ou uma string vazia.
        Este teste é fundamental para garantir que a chave da API Gemini,
        necessária para a comunicação com o serviço, esteja disponível e configurada.
        """
        api_key = self.loader.obter_chave("GEMINI_API_KEY")
        assert api_key is not None, "A variável GEMINI_API_KEY não foi encontrada no .env ou não foi carregada."
        assert api_key != "", "A variável GEMINI_API_KEY está vazia no .env."
