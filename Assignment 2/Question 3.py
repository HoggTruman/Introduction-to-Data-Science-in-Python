import pandas as pd

def chickenpox_by_sex():
    df = pd.read_csv('NISPUF17.csv')
    mf_dict = {"male": len(df[(df['SEX'] == 1) & (df['P_NUMVRC'] > 0) & (df['HAD_CPOX'] == 1)])/len(df[(df['SEX'] == 1) & (df['P_NUMVRC'] > 0) & (df['HAD_CPOX'] == 2)]),
               "female": len(df[(df['SEX'] == 2) & (df['P_NUMVRC'] > 0) & (df['HAD_CPOX'] == 1)])/len(df[(df['SEX'] == 2) & (df['P_NUMVRC'] > 0) & (df['HAD_CPOX'] == 2)])
               }
    return mf_dict

print(chickenpox_by_sex())