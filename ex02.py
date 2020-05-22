import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import variation

QUESTION = '\033[1m'
RESET = '\033[0m'
ANSWER = '\033[94m'
DARK  = '\033[0;30m'
rol = [21, 23, 23, 24, 26, 26, 26, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 29, 29, 29, 30, 30, 30, 30, 30, 30, 30, 31, 31, 31, 32, 32, 32, 32, 33, 33, 33, 34, 34, 34, 34, 34, 36, 36, 37, 37, 39]

media = np.mean(rol)
mediana = np.median(rol)
desvio_padrao = np.std(rol)
moda = stats.mode(rol)[0]
coeficiente_variacao = variation(rol, axis=0)

print(DARK + QUESTION + "a) Calcule a média, desvio padrão, coeficiente de variação, moda e mediana:" + RESET)
print(ANSWER + "Media:", round(media, 2))
print("Desvio padrão:", round(desvio_padrao, 2))
print("Moda:", moda[0])
print("Mediana:", round(mediana, 2))
print("Coeficiente de variação:", round(coeficiente_variacao*100, 2), "% \n")

print(DARK + QUESTION + "b) Construir o histograma dos dados apresentados: " + RESET)
plt.hist(rol, 'doane', histtype='bar',  facecolor='blue', alpha = 0.5, edgecolor = "black")
plt.xlabel('Milhares de $')
plt.ylabel('Semanas')
plt.title('Histograma de Amostra de Vendas de uma firma durante 50 semanas')
plt.grid(True, color='#CCCCCC', linestyle='--', alpha = 0.5)
plt.show()

print(DARK + QUESTION + "c) Classificar o histograma em relação a simetria." + RESET)
print(ANSWER + "Histograma simétrico")
