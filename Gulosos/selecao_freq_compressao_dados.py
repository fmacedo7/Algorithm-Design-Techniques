class CaractereFrequencia:
    def __init__(self, caractere, frequencia):
        self.caractere = caractere
        self.frequencia = frequencia

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

def seleciona_frequencias(texto, num_frequencias):
    frequencias = {}
    for c in texto:
        if c in frequencias:
            frequencias[c] += 1
        else:
            frequencias[c] = 1

    caracteres_frequencias = []
    for caractere, frequencia in frequencias.items():
        caracteres_frequencias.append(CaractereFrequencia(caractere, frequencia))

    caracteres_frequencias.sort(reverse=True)

    selecionadas = caracteres_frequencias[:num_frequencias]

    return selecionadas

texto = "aaabbcddddeeefffff"
num_frequencias = 3
selecionadas = seleciona_frequencias(texto, num_frequencias)
for s in selecionadas:
    print(f"{s.caractere}: {s.frequencia}")