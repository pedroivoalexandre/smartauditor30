# Arquivo: smart_autenticacao/autenticador.py

import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Optional

class Autenticador:
    """
    Classe responsável por verificar a liberação de módulos do projeto SmartAuditor30
    com base em variáveis de ambiente definidas no arquivo .env.
    """

    def __init__(self):
        """
        Inicializa a classe Autenticador.
        Carrega as variáveis de ambiente do arquivo .env localizado em smart_utils/.env.
        """
        # Caminho para o diretório raiz do projeto SmartAuditor30
        project_root = Path(__file__).resolve().parents[2]
        # Caminho para o arquivo .env dentro de smart_utils
        dotenv_path = project_root / 'smart_utils' / '.env'
        load_dotenv(dotenv_path)

    def _obter_variavel(self, nome_variavel: str) -> Optional[str]:
        """
        Método auxiliar interno para obter o valor de uma variável de ambiente.

        Args:
            nome_variavel (str): O nome da variável de ambiente a ser obtida.

        Returns:
            Optional[str]: O valor da variável de ambiente, ou None se não estiver definida.
        """
        return os.getenv(nome_variavel)

    def verificar_modulo(self, modulo: str) -> bool:
        """
        Verifica se um módulo específico está liberado para uso.
        A liberação é determinada pela variável de ambiente LIBERAR_<NOME_DO_MODULO>=true.

        Args:
            modulo (str): O nome do módulo a ser verificado (ex: "SMART_AUTENTICACAO").

        Returns:
            bool: True se o módulo estiver liberado ("true" case insensitive), False caso contrário.
        """
        variavel_liberacao = f"LIBERAR_{modulo.upper()}"
        valor = self._obter_variavel(variavel_liberacao)
        return valor is not None and valor.lower() == "true"

