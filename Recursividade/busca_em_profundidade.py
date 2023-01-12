class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz_adjacencias = [[0] * len(vertices) for _ in range(len(vertices))]

    def adiciona_aresta(self, de, para):
        self.matriz_adjacencias[de][para] = 1
        self.matriz_adjacencias[para][de] = 1

    def busca_profundidade(self, vertice):
        print(vertice.rotulo)  
        vertice.visitado = True

        for i, valor in enumerate(self.matriz_adjacencias[vertice.rotulo]):
            vertice_adjacente = None
            if valor == 1:
                vertice_adjacente = self.vertices[i]
            if vertice_adjacente and not vertice_adjacente.visitado:
                self.busca_profundidade(vertice_adjacente)

vertices = [Vertice(0), Vertice(1), Vertice(2), Vertice(3)]
grafo = Grafo(vertices)
grafo.adiciona_aresta(0, 1)
grafo.adiciona_aresta(0, 2)
grafo.adiciona_aresta(1, 2)
grafo.adiciona_aresta(2, 3)
grafo.busca_profundidade(vertices[0])