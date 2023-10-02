import pandas as pd
import matplotlib.pyplot as plt


#Dados do concurso

data = {
    "bola 1": [1, 1, 1, 3, 1, 1, 2, 1, 1, 3, 3, 1, 1, 1, 2, 2, 3, 1, 4, 2],
    "bola 2": [2, 2, 3, 4, 3, 2, 5, 2, 2, 5, 7, 2, 2, 3, 4, 4, 5, 2, 5, 4],
    "bola 3": [5, 4, 4, 5, 4, 3, 6, 3, 8, 7, 8, 3, 6, 5, 5, 5, 6, 3, 6, 6],
    "bola 4": [7, 6, 5, 6, 6, 4, 9, 4, 9, 8, 9, 4, 9, 6, 6, 6, 9, 4, 7, 7],
    "bola 5": [9, 7, 7, 7, 7, 5, 10, 6, 10, 9, 10, 6, 10, 7, 7, 7, 10, 7, 8, 8],
    "bola 6": [10, 10, 9, 9, 8, 8, 11, 7, 11, 10, 13, 8, 11, 8, 8, 8, 11, 9, 9, 9],
    "bola 7": [12, 14, 12, 13, 11, 9, 13, 8, 12, 13, 14, 9, 12, 11, 10, 10, 13, 11, 10, 13],
    "bola 8": [13, 15, 14, 14, 13, 10, 14, 9, 13, 14, 15, 11, 13, 12, 11, 11, 14, 13, 11, 14],
    "bola 9": [14, 16, 16, 16, 14, 12, 15, 11, 15, 16, 16, 13, 15, 15, 14, 14, 15, 14, 15, 15],
    "bola 10": [17, 17, 18, 17, 15, 17, 18, 13, 17, 17, 19, 14, 17, 16, 15, 16, 16, 15, 16, 16],
    "bola 11": [19, 18, 19, 19, 16, 20, 19, 14, 20, 18, 20, 15, 18, 17, 16, 17, 19, 17, 17, 17],
    "bola 12": [20, 19, 21, 21, 20, 22, 20, 15, 21, 19, 21, 20, 19, 18, 17, 18, 20, 18, 20, 18],
    "bola 13": [21, 21, 22, 22, 22, 23, 21, 16, 22, 20, 23, 21, 20, 19, 20, 19, 21, 19, 21, 19],
    "bola 14": [23, 23, 23, 24, 24, 24, 22, 17, 23, 21, 24, 23, 22, 20, 21, 20, 22, 20, 22, 20],
    "bola 15": [24, 24, 24, 25, 25, 25, 23, 18, 25, 23, 25, 25, 23, 21, 22, 22, 23, 21, 23, 22]
}


#criando um DataFrame a partir dos dados
df = pd.DataFrame(data)

#encontrando os números mais frequentes em todas as bolas
frequencia_numeros = df.iloc[:, 1:].values.flatten()
numeros_mais_frequentes = pd.Series(frequencia_numeros).value_counts()

# Exibindo os números mais frequentes
print("Números mais frequentes:")
print(numeros_mais_frequentes)




# Exibindo os números mais frequentes em um gráfico de barras
numeros_mais_frequentes.plot(kind='bar', figsize=(10, 6))
plt.title('Números Mais Frequentes')
plt.xlabel('Número')
plt.ylabel('Frequência')
plt.show()
