import pandas as pd
import time 
from pandas_datareader import data as web

timeInit = time.time()
df = pd.DataFrame()
acao = 'ABEV3.SA'
df = web.DataReader(acao, data_source='yahoo', start='01-01-2021')
timeEnd = time.time()
print(df.head())
print(f"{timeEnd - timeInit} segundos")

