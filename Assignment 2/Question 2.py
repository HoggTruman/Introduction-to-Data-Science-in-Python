import pandas as pd

def average_influenza_doses():
    df = pd.read_csv('NISPUF17.csv')
    df = df[df['P_NUMFLU'].notna()]
    return (df[df['CBF_01'] == 1]['P_NUMFLU'].sum()/len(df[df['CBF_01'] == 1]),
            df[df['CBF_01'] == 2]['P_NUMFLU'].sum()/len(df[df['CBF_01'] == 2]))



print(average_influenza_doses())