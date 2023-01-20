
def gera_senhas(senha, caracteres, tamanho):
    if len(senha) == tamanho:
        print(senha)
    else:
        for caractere in caracteres:
            gera_senhas(senha + caractere, caracteres, tamanho) #chamada recursiva

caracteres = "abcdefghijklmnopqrstuvwxyz0123456789" #caracteres disponiveis para gerar senhas
tamanho = 2 #tamanho das senhas
gera_senhas("", caracteres, tamanho)