import statistics

# 1 - Aplicar a média
print(statistics.mean([3, 2, 3, 8, 9]))

# 2 - Aplicar a mediana
print(statistics.median([1, 2, 3, 8, 9]))

# 3 - Aplicar a moda
print(statistics.mode([1, 3, 5, 1 ,2, 7, 1, 2]))

# 4 - Desvio padrão
'''
Quanto mais próximo de 0 for o desvio padrão, significa que
os dados do conjuntos estão menos dispersos
'''
print(statistics.stdev([1, 1.2, 2, 2.5, 3, 3.5, 4, 4.5]))
