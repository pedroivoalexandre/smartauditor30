from smart_autenticacao.autenticador import Autenticador

aut = Autenticador()
modulo = "SMART_AUTENTICACAO"

if aut.verificar_modulo(modulo):
    print(f"Acesso ao {modulo}: Liberado")
else:
    print(f"Acesso ao {modulo}: Negado")
