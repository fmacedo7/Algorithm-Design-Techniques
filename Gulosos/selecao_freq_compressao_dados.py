class CaractereFrequencia:
    def __init__(self, caractere, frequencia):
        self.caractere = caractere
        self.frequencia = frequencia

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

def seleciona_frequencias(texto, num_frequencias):
    frequencias = {} # Armazena a frequencia de repetição de cada caractere
    # Conta quantas vezes cada caractere se repete
    for c in texto:
        if c in frequencias:
            frequencias[c] += 1
        else:
            frequencias[c] = 1

    caracteres_frequencias = [] # Armazena os caracteres
    for caractere, frequencia in frequencias.items():
        caracteres_frequencias.append(CaractereFrequencia(caractere, frequencia)) # Armazena os caracteres e quantas vezes se repetem

    caracteres_frequencias.sort(reverse=True) # Ordena de forma decrescente os caracteres que mais se repetem

    selecionadas = caracteres_frequencias[:num_frequencias] # Retorna de os três primeiro caracteres

    return selecionadas

texto = "aaabbcddddeeefffff"
num_frequencias = 3 # A quantidade de carateres que eu quero que retorne
selecionadas = seleciona_frequencias(texto, num_frequencias)
for s in selecionadas:
    print(f"{s.caractere}: {s.frequencia}")