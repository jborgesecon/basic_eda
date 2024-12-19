import pandas as pd
import credentials as cr
import glob
import os


# import and structure both dataframes
dfs = [
    [],     # jg
    []      # tadeu
]

# get files, add to both lists
files = glob.glob("quantitativo\\*.xlsx")
de_para_ccusto = pd.read_csv('datasets\\de_para_ccusto.csv', sep=",")


# add files to the respective list
for file in files:
    fname = os.path.basename(file)
    try:
        current = pd.read_excel(file)
        month = fname[-10:-5]
        current['month'] = month
        dfs[0].append(current) if fname[:2] == 'jg' else dfs[1].append(current)
    except Exception as e:
        print(f'Error reading file {file}: {e}')

# create two separate dataframes using pandas concat
if dfs[0] and dfs[1]:
    df_jg = pd.concat(dfs[0], ignore_index=True)
    df_tadeu = pd.concat(dfs[1], ignore_index=True)
else:
    print('empty dataframe')

print('\n')
distinct_month = df_jg['month'].unique().tolist()
print("Distinct months in df_jg:", distinct_month)

# treating df_jg
df_jg['month'] = pd.to_datetime(df_jg['month'], format='%m-%y')
df_jg['matricula'] = pd.to_numeric(df_jg['matricula'], errors='coerce')
df_jg = df_jg.dropna(subset=['matricula'])
df_jg['MASCARA'] = df_jg['MASCARA'].astype(str)
df_jg['MASCARA'] = df_jg['MASCARA'].str.replace('.0', '')
df_jg['MASCARA'] = df_jg['MASCARA'].str.replace('.', '')
df_jg['MASCARA'] = pd.to_numeric(df_jg['MASCARA'], errors='coerce')


# treating df_tadeu
def map_cc(cc):
    if len(cc) != 11:
        return cc
    
    mapped_value = de_para_ccusto.loc[de_para_ccusto['codccusto'] == cc, 'novo_ccusto'].iloc[0] if (de_para_ccusto['codccusto'] == cc).any() else None
    return mapped_value if pd.notnull(mapped_value) else cc

df_tadeu['centro_de_custo'] = df_tadeu['centro_de_custo'].astype(str)
df_tadeu['cc_index'] = df_tadeu['centro_de_custo'].apply(map_cc)
df_tadeu['cc_index'] = df_tadeu['cc_index'].str.replace('.', '')
df_tadeu['tipo_gestao'] = df_tadeu['tipo_gestao'].str.replace('Gestao Completa', 'GC')
df_tadeu['tipo_gestao'] = df_tadeu['tipo_gestao'].str.replace('Gestao Educacional', 'GE')
# df_tadeu['cc_index'] = df_tadeu['cc_index'].str.replace('-1', '')
df_tadeu['cc_index'] = pd.to_numeric(df_tadeu['cc_index'], errors='coerce')
df_tadeu['matricula'] = pd.to_numeric(df_tadeu['matricula'], errors='coerce')
df_tadeu = df_tadeu.dropna(subset=['matricula'])
df_tadeu['month'] = pd.to_datetime(df_tadeu['month'], format='%m-%y')

# # printing results
# print(df_jg.tail())
# print(df_jg.info())
# print(df_tadeu.tail())
# print(df_tadeu.info())

# print('\n')
# distinct_month = df_jg['month'].unique().tolist()
# print("Distinct months in df_jg:", distinct_month)

# for month in distinct_month:
#     len_jg = df_jg[df_jg['month'] == month].shape[0]
#     len_tadeu = df_tadeu[df_tadeu['month'] == month].shape[0]
#     print(f'{month}: {len_jg} - {len_tadeu}')

# feed to postgres
df_jg.to_sql('quantitativo_jg', cr.st_engine, if_exists='replace', index=False, schema='quantitativo')
df_tadeu.to_sql('quantitativo_tadeu', cr.st_engine, if_exists='replace', index=False, schema='quantitativo')
de_para_ccusto.to_sql('de_para_cc', cr.st_engine, if_exists='replace', index=False, schema='quantitativo')

print("DataFrames loaded to 'quantitativo' schema successfully.")