# tests/test_gemini_api_key.py

# Este arquivo de teste é crucial para verificar a integração do projeto com a API Gemini.
# Ele garante que a `GEMINI_API_KEY` configurada no arquivo `.env` é válida e funcional,
# realizando uma chamada real à API. Isso serve como um teste de integração,
# confirmando que a comunicação com o serviço externo está operando conforme o esperado.

import os
import pytest
from pathlib import Path
import google.generativeai as genai
from smart_utils.env_loader import EnvLoader

class TestGeminiAPIKey:
    """
    Classe de teste para verificar a validade e funcionalidade da chave da API Gemini.
    Realiza uma chamada de teste à API para confirmar a autenticação e a resposta.
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

    def test_gemini_api_key_validity(self):
        """
        Verifica a validade da `GEMINI_API_KEY` fazendo uma chamada funcional à API Gemini via SDK.
        Este teste:
        1. Obtém a chave da API usando o `EnvLoader`.
        2. Ignora o teste se a chave for ausente, padrão ou suspeita (muito curta).
        3. Configura a chave da API para o SDK do Gemini.
        4. Tenta gerar conteúdo usando o modelo `gemini-1.5-flash`.
        5. Afirma que a resposta da API não está vazia.
        6. Em caso de erro na conexão ou na validade da chave, o teste falha.
        """
        api_key = self.loader.obter_chave("GEMINI_API_KEY")
        print(f"🔑 Chave sendo usada: {api_key}")

        if not api_key or api_key == "sua_chave_aqui" or len(api_key.strip()) < 10:
            pytest.skip("GEMINI_API_KEY ausente, é o valor padrão ou suspeita (curta demais).")

        try:
            genai.configure(api_key=api_key)
            modelo = genai.GenerativeModel("gemini-1.5-flash")
            resposta = modelo.generate_content("Olá! Você está funcionando?")
            assert resposta.text.strip() != "", "A resposta da API Gemini está vazia."
            print("✅ Chave válida e resposta recebida:", resposta.text.strip())
        except Exception as e:
            pytest.fail(f"❌ Erro ao conectar à API Gemini: {e}")
