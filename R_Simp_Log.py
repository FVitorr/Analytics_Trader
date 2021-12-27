'''
Para explorar o potencial de algum ativo na bolsa uma das
análises fundamentais mais simples que podemos fazer se refere 
ao calculo da taxa de retorno simples e logarítmica

--> Calcular o percentual da taxa de retorno de um investimento .
--> Comparar com outros investimentos.
'''

import numpy as np 
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

AMZN = wb.DataReader('AMZN', data_source='yahoo', start ='2000-01-01')
print(AMZN.head())

'''
Taxa de retorno simples é determinada pela razão entre o preço final
menos o preço inicial sobre o preço inicial

normalmente é utilizada quando queremos lidar com vários ativos ao
mesmo tempo.
'''
AMZN['simple_return'] = (AMZN['Adj Close'] / AMZN['Adj Close'].shift(1)) - 1
print (AMZN['simple_return'])
AMZN['simple_return'].plot(figsize=(8,5))
plt.show()
retorno_medio_diario = AMZN['simple_return'].mean() * 250
print(f"Retorno Medio Diario: {round(retorno_medio_diario,5) * 100}")

'''
A taxa de retorn logarítimica é calculada pelo log da razão entre Preço
final e Preço inicial

Já a taxa de retorno logarítmica é preferível quando realizamos
cálculos sobre um único ativo ao longo de um período de tempo.
'''
## Criando nova coluna com os valores de log return
AMZN['log_return'] = np.log(AMZN['Adj Close']/AMZN['Adj Close'].shift(1))
AMZN['log_return'].plot(figsize=(8,5))
plt.show()
## Calculando o retorno médio diário ao longo do tempo
retorno_medio_diario_log = AMZN['log_return'].mean() * 250
print(f"Retorno Medio Diario {round(retorno_medio_diario_log, 5) * 100}")




















