# distância de Levenshtein

# 0 - A função distancia_edicao recebe como argumentos duas strings, s1 e s2, e retorna a distância de edição entre elas;

# 1 - Inicialização da tabela: uma tabela 2D é criada com o tamanho de len(s1) + 1 linhas e len(s2) + 1 colunas. 
#     Cada elemento da tabela é inicializado com 0;

# 2 -  Preenchimento da primeira linha e coluna: A primeira linha e coluna são preenchidas com os índices i e j, respectivamente. 
#      Isso representa o número mínimo de operações necessárias para transformar uma string vazia em s1 ou s2;

# 3 - Preenchimento da tabela: um loop interno é usado para percorrer as linhas da tabela, 
#     começando da linha 1 e coluna 1. Para cada par de caracteres nas strings s1 e s2, se eles forem iguais, 
#     o valor na tabela é preenchido com o valor da célula imediatamente acima e à esquerda. Caso contrário, 
#     o valor na tabela é preenchido com o menor dos três valores: o valor da célula imediatamente acima e à esquerda, 
#     o valor da célula imediatamente acima ou o valor da célula imediatamente à esquerda, mais 1;

# 4 - Retorno da distância de edição: a função retorna o valor na última célula da tabela, que representa a distância de edição entre s1 e s2.

def distancia_edicao(s1, s2):
    tabela = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)] 
    for i in range(len(s1)+1):
        tabela[i][0] = i
        for j in range(len(s2)+1):
            tabela[0][j] = j
            for i in range(1, len(s1)+1):
                for j in range(1, len(s2)+1):
                    if s1[i-1] == s2[j-1]:
                        tabela[i][j] = tabela[i-1][j-1]
                    else:
                        tabela[i][j] = min(tabela[i-1][j-1] + 1, tabela[i-1]
                                [j] + 1, tabela[i][j-1] + 1)
            return tabela[len(s1)][len(s2)]
print(distancia_edicao("aaaa", "bcda"))  # 3
#print(distancia_edicao("kitten", "sitting"))  # 3
#print(distancia_edicao("gumbo", "gambol")) # 2