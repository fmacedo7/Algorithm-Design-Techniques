import random

def gera_senha(tamanho, senha_atual, caracteres_permitidos):
    if len(senha_atual) == tamanho:
        return senha_atual
    random.shuffle(caracteres_permitidos)
    for caractere in caracteres_permitidos:
        nova_senha = gera_senha(tamanho, senha_atual + caractere, caracteres_permitidos)
        if len(nova_senha) == tamanho:
            return nova_senha
    return senha_atual

caracteres = list("abcdefghijklmnopqrstuvwxyz0123456789")
tamanho = 8
senha = gera_senha(tamanho, "", caracteres)
print(senha)