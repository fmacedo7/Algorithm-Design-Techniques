def busca_binaria(lista, elemento):
    meio = len(lista) // 2
    if elemento == lista[meio]:
        return True
    if len(lista) == 1:
        return False
    if elemento < lista[meio]:
        return busca_binaria(lista[:meio], elemento)
    else:
        return busca_binaria(lista[meio+1:], elemento)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(busca_binaria(lista, 2))
print(busca_binaria(lista, 10))