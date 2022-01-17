import scipy.stats as stats
import pandas as pd

def corr_chickenpox():
    df = pd.read_csv('NISPUF17.csv')
    df = df[df['HAD_CPOX'].notna() & df['P_NUMVRC'].notna()]
    df = df[df['HAD_CPOX'].isin([1, 2])]

    return stats.pearsonr(df['HAD_CPOX'], df['P_NUMVRC'])[0]

print(corr_chickenpox())