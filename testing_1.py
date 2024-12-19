import pandas as pd
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

def map_cc(cc):
    if len(cc) != 11:
        return cc
    
    mapped_value = de_para_ccusto.loc[de_para_ccusto['codccusto'] == cc, 'novo_ccusto'].iloc[0] if (de_para_ccusto['codccusto'] == cc).any() else None
    return mapped_value if pd.notnull(mapped_value) else cc

df_tadeu['centro_de_custo'] = df_tadeu['centro_de_custo'].astype(str)
df_tadeu['cc_index'] = df_tadeu['centro_de_custo'].apply(map_cc)
