import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


path = {
    'main': 'arthur\\base_2.csv',
    'patient': 'arthur\\paciente.csv'
}

df_main = pd.read_csv(path['main'], encoding='latin1', sep=';')
df_patient = pd.read_csv(path['patient'], encoding='latin1', sep=';')

df_main['Data_nasc'] = pd.to_datetime(df_main['Data_nasc'], origin='1899-12-30', unit='D')
df_main = df_main.drop(columns=['Tempo_sint_>30'])

def tempo_sintoma(c):
    if c > 30:
        return 1
    elif 1 <= c <= 30:
        return 0
    elif c <= 0:
        return np.nan

df_main['Tempo_sint_>30'] = df_main['Temp_sint_dias'].apply(tempo_sintoma)
cols = df_main.columns.to_list()
for col in cols:
    # print(col)
    pass

cols_info = [
'Prontua',
'Nome',
'Sexo',
'Data_nasc',
'Idade',
'grupo2',
'Escore_risco',
'Eventos'
]

cols_detalhes = [
'Temp_sint_mês',
'Temp_sint_dias',
'Tempo_sint_>30',
'Dias_inter',
'Buscas_prévias_saúde'
]

cols_exames = [
'Htc_D1',
'Hgb_D1',
'Htc_D30',
'Hgb_30',
'Leuc_D1',
'Leuc_D30',
'Neut_D1',
'Neut_D30',
'Plat_D1',
'Plat_D30',
'INR',
'Ureia',
'Creat',
'AST',
'ALT',
'BT',
'PT',
'Albumina',
'Globulina',
'Triglicerides',
'CT',
'LDL',
'HDL',
'Ferritina',
'VHS',
'LDH',
'Fibrinogenio',
'PCR'
]

cols_medicamento = [
'Ampicilina Sulbactam',
'Bactrim',
'Cefepime',
'Cetoconazol',
'Cipro',
'Clofazimina',
'Dapsona',
'Fluconazol',
'Imipinem',
'Ivermectina',
'Levofloxacina',
'Mero',
'Metronidazol',
'Moxifloxacina',
'Permetrina',
'Vanco'
]

cols_sintomas = [
'Febre',
'Taquic',
'Taquip',
'Sud',
'Esplenome',
'Hepatome',
'Astenia',
'Perda_pond',
'Dispneia',
'Hiporexia',
'Palidez',
'Sangramento',
'Diarreia',
'Edema',
'Ascite',
'Adenopatia',
'Dor_abd',
'Ictericia',
'Comorbidades',
'HAS',
'DM',
'Infection',
'Microscopia',
'rk9',
'IgM',
'IFI',
'HIV',
'Transfusion',
'Reation',
'Anemia',
'Leucopenia',
'Neutropenia',
'Neutrop_febril',
'Trombocitopenia',
'Tromb_<50k',
'Pancito',
'Coagulopatia',
'Ins_renal',
'High_ferritin',
'Estrato_risco',
'Risco_alto',
'Rec_falha',
'Morte'
]


# print(df_main[cols_detalhes].sort_values('Dias_inter'))
# dias = sorted(df_main['Dias_inter'].to_list())
# print(dias)
# print(len(dias))
aba = ['grupo2', 'Dias_inter']
df2 = df_main[aba]
df2 = df2.sort_values(by='Dias_inter')
n = len(df2)
part = n // 4

groups2 = list()
for i in range(4):
    start_index = i * part
    if i == 3:
        end_index = n
    else:
        end_index = (i+1)*part

    groups2.append(df2.iloc[start_index:end_index])

for idx, group in enumerate(groups2):
    print(f'Group {idx + 1}:')
    print(group)

# pacientes_total = df_main.groupby('grupo2')['Prontua'].nunique().reset_index()
pacientes_total = df_main.groupby('grupo2')['Prontua'].count().reset_index()
pacientes_total = pacientes_total.rename(columns={'Prontua': 'total'})

sem_crithidia = pacientes_total[pacientes_total['grupo2'].isin(['B', 'C'])]['total'].sum()
sem_crithidia_df = pd.DataFrame({'grupo2': ['B+C'], 'total': [sem_crithidia]})
pacientes_total = pd.concat([pacientes_total, sem_crithidia_df], ignore_index=True)



# print(pacientes_total)