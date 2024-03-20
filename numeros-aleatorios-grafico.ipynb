from scipy import stats
import matplotlib.pyplot as plt
from random import uniform
import numpy as np

##### escolhendo a quantidade de números aleatórios:
quant_num = int(input('Escolha uma quantidade de números aleatórios: '))

lista = []
for elemento in range(quant_num):
    numero_aleatorio = uniform(0, 100)
    lista.append(numero_aleatorio)
lista_ordenada = sorted(lista)
print(f'Os elementos da lista são: {lista_ordenada}')

## maximos e minimos
menor_valor = min(lista)
maior_valor = max(lista)
print(f'O menor valor que há lista é {menor_valor:.2f} e o maior valor é {maior_valor:.2f}')

#soma dos elementos da lista
soma_dos_elementos = sum(lista)
print(f'A soma dos elementos da lista dá: {soma_dos_elementos:.2f}')

# media e desvio padrão
media = (soma_dos_elementos/quant_num)  # poderia usar len(lista)
print(f'A média é de {media:.2f}')
desvio_padrao = np.std(lista)
print(f'O desvio padrão é {desvio_padrao:.2f}')


# Ajustando o tamanho do gráfico
plt.figure(figsize=(12, 8))  # Tamanho do gráfico em polegadas (largura, altura)

# Preparando os dados para o gráfico
indices = range(quant_num)  # Índices para o eixo x dos dados

# Plotando os dados
plt.scatter(indices, lista, color='green', label='Dados')

# Linhas para a média e desvio padrão
plt.axhline(y=media, color='blue', linestyle='-', linewidth=2, label='Média')
plt.axhline(y=media + desvio_padrao, color='orange', linestyle='--', linewidth=2, label='Média + Desvio Padrão')
plt.axhline(y=media - desvio_padrao, color='orange', linestyle='--', linewidth=2, label='Média - Desvio Padrão')

# Adicionando título e rótulos
plt.title('Dispersão dos Dados com Média e Desvio Padrão')
plt.xlabel('Índice dos Dados')
plt.ylabel('Valores')
plt.xticks(indices)  # Configura os ticks do eixo x para corresponder aos índices dos dados
plt.legend()  # Adiciona a legenda

# Mostra o gráfico
plt.show()



## CÁLCULO DA REGRESSÃO LINEAR

# Ajustando a regressão linear aos dados
slope, intercept, r_value, p_value, std_err = stats.linregress(indices, lista)

# Criando valores para a linha de regressão
line = [slope * x + intercept for x in indices]

## GRÁFICO DE REGRESSÃO LINEAR

plt.figure(figsize=(12, 8))  # Tamanho do gráfico

plt.scatter(indices, lista, color='green', label='Dados Originais')  #legenda do gráfico
plt.plot(indices, line, color='red', label='Linha de Regressão')     #legenda

plt.title('Regressão Linear dos Dados')
plt.xlabel('Índice dos Dados')
plt.ylabel('Valores')
plt.xticks(indices)
plt.legend()

plt.show()
