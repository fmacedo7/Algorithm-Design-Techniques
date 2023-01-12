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
print(distancia_edicao("kitten", "sitting"))  # 3  
print(distancia_edicao("gumbo", "gambol")) # 2