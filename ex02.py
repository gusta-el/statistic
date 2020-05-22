import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import variation

def getLinhas(rol):
    media = np.mean(rol)
    mediana = np.median(rol)
    amplitude = max(rol) - min(rol)
    variancia = np.var(rol)
    desvio_padrao = np.std(rol)
    data = [round(media, 2), round(mediana, 2), round(amplitude, 2), round(variancia, 2), round(desvio_padrao, 2)]
    return data

QUESTION = '\033[1m'
RESET = '\033[0m'
ANSWER = '\033[94m'
DARK  = '\033[0;30m'

rol = [1434, 3692, 4482, 4119, 1043, 4520, 432, 618, 4564, 4086, 4371, 2918, 141, 127, 929, 3130, 3174, 2181, 559, 940, 5123, 5674, 1423, 1316, 901, 943, 3041, 3870, 5564, 353, 1161, 1732, 3322, 8608, 659]
eua_value = 8608

row_labels = ["Média", "Mediana", "Amplitude", "Variância", "Desvio Padrão"]
col_labels = ["Com EUA", "Sem EUA"]

com_eua = getLinhas(rol)
rol.remove(eua_value)
sem_eua = getLinhas(rol)

table_data = [[0,0],[0,0],[0,0],[0,0],[0,0]]
for x in range(0,5):
    table_data[x] = [com_eua[x], sem_eua[x]]

fig = plt.figure(dpi=65)
ax = fig.add_subplot(1,1,1)
table = ax.table(cellText=table_data, loc='center', rowLabels=row_labels, colLabels=col_labels)
table.set_fontsize(14)
table.scale(1,3)

ax.axis('off')


print(DARK + QUESTION + "Ache a média das despesas com cuidados da saúde nesses países, com e sem os Estados Unidos.")
print("Faça os seguintes cálculos (use calculadora ou o computador):")

plt.show()

print(DARK + QUESTION + "Qual o impacto desse valor atípico?"+ RESET)
print(ANSWER + "Este impacto faz com que valores como média e amplitude se alterem de forma significativa pois são muito influenciados por seus outliers.")
