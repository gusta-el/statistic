import numpy as np
import math as calc

QUESTION = '\033[1m'
RESET = '\033[0m'
ANSWER = '\033[94m'
DARK  = '\033[0;30m'

print(DARK + QUESTION + "3) Um analista possui as seguintes informações a respeito dos valores a de uma amostra de 30 observações:"+ RESET)
print("- A média de todos os valores é igual a 2.96 ")
print("- A soma dos quadrados dos valores é igual 268 Calcule o desvio padrão amostral")
print(DARK + QUESTION + "Calcule o desvio padrão amostral. "+ RESET)

media = 2.96
n = 30
xi2_soma = 268
xi_soma = media * n

variancia = (1 / (n - 1)) * (xi2_soma - ((1 / n) * (xi_soma * xi_soma)))
desvio_padrao_amostral = calc.sqrt(variancia)

print(ANSWER + "Desvio padrão amostral: ", round(desvio_padrao_amostral, 2))
