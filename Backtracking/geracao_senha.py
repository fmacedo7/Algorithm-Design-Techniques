def gera_senhas(senha, caracteres, tamanho):
    password = "99"
    if len(senha) == tamanho and password:
        print("A senha e: " + senha)
    else: 
        for caractere in caracteres:
            gera_senhas(senha + caractere, caracteres, tamanho) #chamada recursiva

caracteres = "abcdefghijklmnopqrstuvwxyz0123456789" #caracteres disponiveis para gerar senhas
tamanho = 2 #tamanho das senhas
gera_senhas("", caracteres, tamanho)