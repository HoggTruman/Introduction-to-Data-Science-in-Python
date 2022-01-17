from Question1 import answer_one

import scipy.stats as stats

def answer_nine():
    df = answer_one()
    df['pop'] = df['Energy Supply'] / df['Energy Supply per Capita']
    df['cdpp'] = df['Citable documents']/df['pop']

    return stats.pearsonr(df['cdpp'], df['Energy Supply per Capita'])[0]

if __name__ == "__main__":
    print(answer_nine())