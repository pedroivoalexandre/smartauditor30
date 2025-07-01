import os
from dotenv import load_dotenv
from pathlib import Path

class EnvLoader:
    """Carrega variáveis de ambiente de um arquivo .env."""

    def __init__(self, caminho_env):
        """
        Inicializa o EnvLoader com o caminho para o arquivo .env.

        Args:
            caminho_env (str or Path): O caminho para o arquivo .env.
        """
        if not isinstance(caminho_env, Path):
            caminho_env = Path(caminho_env)
        
        if not caminho_env.is_file():
            raise FileNotFoundError(f"O arquivo .env não foi encontrado em: {caminho_env}")
            
        self.caminho_env = caminho_env
        self.carregar()

    def carregar(self):
        """Carrega as variáveis do arquivo .env para o ambiente."""
        load_dotenv(dotenv_path=self.caminho_env)

    def obter_chave(self, nome_variavel):
        """
        Obtém o valor de uma variável de ambiente.

        Args:
            nome_variavel (str): O nome da variável a ser obtida.

        Returns:
            str or None: O valor da variável de ambiente ou None se não for encontrada.
        """
        return os.getenv(nome_variavel)
