import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


path = {
    'subcontas': 'fat_dre\\subcontas.xlsx',
    'detalhada': 'fat_dre\\detalhada.xlsx'
}

df_subcontas = pd.read_excel(path['subcontas'])
df_detalhada = pd.read_excel(path['detalhada'])

cols = [
    'idpartida', 
    'data', 
    'reduzida', 
    'descricao', 
    'codccusto', 
    'CC_INDEX', 
    'NOME_CC', 
    'complemento', 
    'lancamento', 
    'm_conta'
]

# Exploratory data analysis

df_subcontas[cols[-1]] = df_subcontas[cols[-1]].astype(str)
filtered1 = df_subcontas[~df_subcontas['m_conta'].str.contains('RECEITA', case=False)]
print(filtered1)
# print(df_subcontas[cols[-1]].unique())
# result = df_subcontas.groupby(cols[-3])[cols[-2]].sum().reset_index()
# result = result.sort_values(by=cols[-2], ascending=True)

# print(result)