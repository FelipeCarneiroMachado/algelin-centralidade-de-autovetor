import numpy as np

#Input
vertex, edges = map(int, input().split())
graph = np.zeros((vertex, vertex), dtype=np.float64)
for _ in range(edges):
    inp = input().split()
    graph[tuple(map(lambda x: int(x) - 1, inp[:2]))] = float(inp[2])
graph = graph * 2



#Caso as condicoes do teorema de ferron-frobenius sejam satisfeitas
#Basta pegar o maior autovalor e seu autovetor correspondente e encontrar a maior medida
#de centralidade neste autovetor
#AutoValores e auto vetores
eigv = np.linalg.eig(graph.T)
print(abs(eigv.eigenvectors[:,eigv.eigenvalues.argmax()]).argmax() + 1)
