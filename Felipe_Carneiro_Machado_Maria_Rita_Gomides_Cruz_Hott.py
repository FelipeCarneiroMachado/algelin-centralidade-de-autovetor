import numpy as np
import networkx as nx

#Input
vertex, edges = map(int, input().split())
graph = np.zeros((vertex, vertex), dtype=np.float64)
for _ in range(edges):
    inp = input().split()
    graph[tuple(map(lambda x: int(x) - 1, inp[:2]))] = float(inp[2])
graph = graph * float(input())

#Cria o grafo no networkx para poder utilizar a funcao is_connected
nx_graph = nx.from_numpy_array(graph)

#O teorema de perron-frobenius requewer que a matriz seja estritamente positivo
#ou nao negativo e irredutivel
#uma matriz ser irredutivel eh equivalente ao grafo que ela representa ser 
#fortemente conexo

#verifica se qh maior que zero
if np.any(graph == 0):
    if not nx.is_connected(nx_graph):
        print("Bixo SemVerTonha")
        exit(0)

#Caso as condicoes do teorema de ferron-frobenius sejam satisfeitas
#Basta pegar o maior autovalor e seu autovetor correspondente e encontrar a maior medida
#de centralidade neste autovetor
#AutoValores e auto vetores
eigv = np.linalg.eig(graph.T)
print(eigv.eigenvectors[:,eigv.eigenvalues.argmax()].argmax() + 1)
