from Question1 import answer_one
import pandas as pd


def answer_twelve():
    df = answer_one()
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
    df['Continent'] = df.index.to_series().map(ContinentDict)
    df['% Renewable'] = pd.cut(df['% Renewable'], 5)

    s = df.groupby(['Continent', '% Renewable']).size()

    return s[s != 0]


if __name__ == "__main__":
    print(answer_twelve())
