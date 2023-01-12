import random

def gera_senha(tamanho, senha_atual, caracteres_permitidos):
    # Se a senha atual tem o tamanho desejado, retorna a senha
    if len(senha_atual) == tamanho:
        return senha_atual
    # embaralha a lista de caracteres permitidos
    random.shuffle(caracteres_permitidos)
    # para cada caractere permitido
    for caractere in caracteres_permitidos:
        # chama recursivamente a função passando a senha atual mais o caractere 
        nova_senha = gera_senha(tamanho, senha_atual + caractere, caracteres_permitidos)
        # se a nova senha tiver o tamanho desejado, retorna a senha
        if len(nova_senha) == tamanho:
            return nova_senha
    return senha_atual

caracteres = list("abcdefghijklmnopqrstuvwxyz0123456789")
tamanho = 8
senha = gera_senha(tamanho, "", caracteres)
print(senha)