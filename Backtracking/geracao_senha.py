import random

def gera_senhas(senha, caracteres, tamanho):
    if len(senha) == tamanho:
        print(senha)
    else:
        for caractere in caracteres:
            gera_senhas(senha + caractere, caracteres, tamanho)

caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"
tamanho = 4
gera_senhas("", caracteres, tamanho)
