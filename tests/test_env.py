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

def test_gemini_api_key():
    """
    Testa o carregamento e a verificação da GEMINI_API_KEY usando EnvLoader.
    """
    # Constrói o caminho para o arquivo .env de forma robusta
    caminho_env = Path(__file__).resolve().parent.parent / 'smart_utils' / '.env'
    
    # 1. Cria uma instância do EnvLoader, que já carrega as variáveis
    loader = EnvLoader(caminho_env)
    
    # 2. Obtém a chave
    api_key = loader.obter_chave("GEMINI_API_KEY")
    
    # 3. Verifica com assert
    assert api_key is not None, "A variável GEMINI_API_KEY não foi encontrada."
    assert api_key == "sua_chave_aqui", "O valor da GEMINI_API_KEY não é o esperado."
