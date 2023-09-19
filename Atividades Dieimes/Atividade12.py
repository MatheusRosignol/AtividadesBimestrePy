import numpy as np

# Crie uma matriz 3x3 usando NumPy
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Percorra e imprima cada elemento da matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()  # Pule para a próxima linha após cada linha da matriz