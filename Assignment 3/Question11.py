import pandas

from Question1 import answer_one
import pandas as pd
import numpy as np


def answer_eleven():
    df = answer_one()
    df['pop'] = df['Energy Supply'] / df['Energy Supply per Capita']
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}

    cdf = df.groupby(ContinentDict)

    new_df = pd.DataFrame(index=cdf.indices, columns=['size', 'sum', 'mean', 'std'])
    new_df['size'] = cdf['pop'].count()
    new_df['sum'] = cdf['pop'].sum()
    new_df['mean'] = cdf['pop'].mean()
    new_df['std'] = cdf['pop'].std()
    print(new_df)
    return new_df


if __name__ == "__main__":
    print(answer_eleven())
