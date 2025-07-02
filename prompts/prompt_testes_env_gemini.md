# 🧪 Prompt de Geração de Testes para `.env` e API Gemini

## 🔧 Objetivo

Criar testes automatizados em Python para:

1. Verificar o carregamento correto do arquivo `.env`.
2. Garantir que a variável `GEMINI_API_KEY` está presente e não está vazia.
3. Validar a chave fazendo uma chamada real à API Gemini via SDK oficial `google-generativeai`.

---

## 📂 Estrutura do Projeto

- A classe `EnvLoader` está localizada em:  
  `smart_utils/env_loader.py`

- O arquivo `.env` está localizado em:  
  `smart_utils/.env`

- Os testes estão organizados da seguinte forma:
  - Testes gerais:  
    `tests/`
  - Testes específicos de módulos:  
    `smart_autenticacao/tests/`, `smart_core/tests/`, etc.

---

## 📌 Regras para os Testes

- Use `Path` do `pathlib` para montar o caminho até o `.env`
- Utilize `pytest.fixture(autouse=True)` para o setup do loader
- A variável deve ser lida via:  
  `self.loader.obter_chave("GEMINI_API_KEY")`
- Configure a API com:  
  `genai.configure(api_key=...)`
- Use o modelo: `"gemini-1.5-flash"`
- Teste a chave com:  
  `model.generate_content("Olá! Você está funcionando?")`
- Verifique se `resposta.text.strip()` não está vazia
- Use `pytest.skip()` se a chave estiver ausente ou for `"sua_chave_aqui"`
- Em caso de erro, use `pytest.fail("mensagem")`

---

## 🧪 Bibliotecas Utilizadas

- `pytest`
- `google-generativeai`
- `dotenv`
- `os`
- `pathlib`

---

## 🗂️ Arquivos Esperados

### `tests/test_env_loading.py`

- Verifica se o arquivo `.env` está presente
- Valida se `GEMINI_API_KEY` existe e não está vazia

### `tests/test_gemini_api_key.py`

- Realiza a validação real da chave usando o SDK
- Integra com `EnvLoader`
- Verifica se a chave permite chamada bem-sucedida ao modelo `gemini-1.5-flash`

---

## ✅ Pré-requisitos

- Certifique-se de que as dependências do projeto estão instaladas.
- Você pode instalar os pacotes necessários com:

```bash
pip install -r requirements.txt
